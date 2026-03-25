"""
HBF Customer Satisfaction Survey Scraper
-----------------------------------------
Scrapes the rolling 12-month data table from the HBF website and
saves results to a CSV file for analysis.

Usage:
    pip install requests beautifulsoup4 pandas
    python hbf_scraper.py

Output:
    hbf_satisfaction_data.csv
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import time
import sys

# ── Config ─────────────────────────────────────────────────────────────────

URL = "https://www.hbf.co.uk/policy/customer-satisfaction-survey/results/"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-GB,en;q=0.9",
}

OUTPUT_FILE = "hbf_satisfaction_data.csv"

# ── Scraper ─────────────────────────────────────────────────────────────────

def fetch_page(url: str) -> BeautifulSoup:
    """Fetch a URL and return a BeautifulSoup object."""
    print(f"  Fetching: {url}")
    try:
        response = requests.get(url, headers=HEADERS, timeout=15)
        response.raise_for_status()
        return BeautifulSoup(response.text, "html.parser")
    except requests.exceptions.HTTPError as e:
        print(f"  HTTP error: {e}")
        sys.exit(1)
    except requests.exceptions.ConnectionError:
        print("  Connection error — check your internet connection.")
        sys.exit(1)
    except requests.exceptions.Timeout:
        print("  Request timed out.")
        sys.exit(1)


def extract_tables(soup: BeautifulSoup) -> list[pd.DataFrame]:
    """Find all HTML tables on the page and return as DataFrames."""
    tables = soup.find_all("table")
    if not tables:
        print("  No tables found on page.")
        return []

    print(f"  Found {len(tables)} table(s) on page.")
    dataframes = []

    for i, table in enumerate(tables):
        rows = []
        headers = []

        # Extract headers
        header_row = table.find("thead")
        if header_row:
            headers = [th.get_text(strip=True) for th in header_row.find_all(["th", "td"])]

        # Extract body rows
        tbody = table.find("tbody") or table
        for tr in tbody.find_all("tr"):
            cells = [td.get_text(strip=True) for td in tr.find_all(["td", "th"])]
            if cells:
                rows.append(cells)

        if not rows:
            continue

        # Build DataFrame
        if headers and len(headers) == len(rows[0]):
            df = pd.DataFrame(rows, columns=headers)
        else:
            df = pd.DataFrame(rows)
            if headers:
                # Headers may be the first row
                df.columns = [f"col_{j}" for j in range(len(df.columns))]

        # Drop fully empty rows
        df = df.dropna(how="all")
        df = df[~df.apply(lambda r: r.astype(str).str.strip().eq("").all(), axis=1)]

        if not df.empty:
            dataframes.append(df)
            print(f"  Table {i+1}: {len(df)} rows × {len(df.columns)} columns")

    return dataframes


def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """Basic cleaning — strip whitespace, normalise column names."""
    df.columns = [
        str(c).strip().lower()
        .replace(" ", "_")
        .replace("%", "pct")
        .replace("?", "")
        .replace("'", "")
        .replace("(", "")
        .replace(")", "")
        for c in df.columns
    ]
    for col in df.columns:
        df[col] = df[col].astype(str).str.strip()
    return df


def save_results(dataframes: list[pd.DataFrame], output_file: str):
    """Save all tables to a single CSV, separated by a blank row."""
    if not dataframes:
        print("  Nothing to save.")
        return

    # If there's one table, save it directly
    if len(dataframes) == 1:
        df = clean_dataframe(dataframes[0])
        df.to_csv(output_file, index=False)
        print(f"\n  Saved {len(df)} rows to {output_file}")
        return

    # Multiple tables — stack with a separator
    combined_parts = []
    for i, df in enumerate(dataframes):
        df = clean_dataframe(df)
        df.insert(0, "table_number", i + 1)
        combined_parts.append(df)

    combined = pd.concat(combined_parts, ignore_index=True)
    combined.to_csv(output_file, index=False)
    print(f"\n  Saved {len(combined)} rows across {len(dataframes)} tables to {output_file}")


def print_preview(dataframes: list[pd.DataFrame]):
    """Print a preview of each table found."""
    if not dataframes:
        return
    print("\n── Preview ─────────────────────────────────────────────────────")
    for i, df in enumerate(dataframes):
        print(f"\nTable {i+1}:")
        print(df.head(10).to_string(index=False))
    print("\n────────────────────────────────────────────────────────────────")


# ── Main ────────────────────────────────────────────────────────────────────

def main():
    print("\n── HBF Satisfaction Data Scraper ───────────────────────────────")
    print(f"  Target: {URL}")
    print(f"  Output: {OUTPUT_FILE}")
    print(f"  Time:   {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("────────────────────────────────────────────────────────────────\n")

    # 1. Fetch the page
    print("Step 1: Fetching page...")
    soup = fetch_page(URL)

    # 2. Extract tables
    print("\nStep 2: Extracting tables...")
    dataframes = extract_tables(soup)

    if not dataframes:
        # The table may be loaded dynamically — try looking for embedded data
        print("\n  No static tables found.")
        print("  The data may be loaded dynamically (JavaScript).")
        print("  Try the manual download method below:\n")
        print("  1. Go to: https://www.hbf.co.uk/policy/customer-satisfaction-survey/results/")
        print("  2. Right-click the table → 'Copy' → paste into Excel or Google Sheets")
        print("  3. Or use your browser's DevTools (F12) → Network tab → look for JSON/XHR requests")
        return

    # 3. Preview
    print_preview(dataframes)

    # 4. Save
    print("Step 3: Saving to CSV...")
    save_results(dataframes, OUTPUT_FILE)

    print("\nDone! Open hbf_satisfaction_data.csv in Excel or run analysis.py to visualise.")
    print("────────────────────────────────────────────────────────────────\n")


if __name__ == "__main__":
    main()
