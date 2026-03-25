"""
HBF Data Analyser
------------------
Once you have hbf_satisfaction_data.csv from hbf_scraper.py,
run this script to print a ranked table and spot the key gaps.

Usage:
    pip install pandas
    python analyse.py
"""

import pandas as pd
import sys
import os

INPUT_FILE = "hbf_satisfaction_data.csv"

# Major builders to highlight
MAJOR_BUILDERS = [
    "barratt", "redrow", "taylor wimpey", "persimmon",
    "bellway", "vistry", "berkeley", "bloor", "keepmoat",
    "miller", "bovis", "countryside", "crest"
]


def load_data(path: str) -> pd.DataFrame:
    if not os.path.exists(path):
        print(f"  File not found: {path}")
        print("  Run hbf_scraper.py first.")
        sys.exit(1)
    df = pd.read_csv(path)
    print(f"  Loaded {len(df)} rows, {len(df.columns)} columns.")
    print(f"  Columns: {list(df.columns)}\n")
    return df


def find_score_column(df: pd.DataFrame) -> str | None:
    """Try to identify the satisfaction % column."""
    for col in df.columns:
        if any(kw in col for kw in ["pct", "score", "recommend", "yes", "%", "satisfaction"]):
            return col
    return None


def find_builder_column(df: pd.DataFrame) -> str | None:
    """Try to identify the builder name column."""
    for col in df.columns:
        if any(kw in col for kw in ["builder", "company", "name", "developer", "housebuilder"]):
            return col
    # Fall back to first column
    return df.columns[0]


def analyse(df: pd.DataFrame):
    builder_col = find_builder_column(df)
    score_col = find_score_column(df)

    print(f"  Builder column: {builder_col}")
    print(f"  Score column:   {score_col or 'not detected — showing raw data'}\n")

    if score_col:
        # Clean score column — strip %, convert to numeric
        df[score_col] = (
            df[score_col]
            .astype(str)
            .str.replace("%", "", regex=False)
            .str.strip()
        )
        df[score_col] = pd.to_numeric(df[score_col], errors="coerce")
        df = df.dropna(subset=[score_col])
        df = df.sort_values(score_col, ascending=False)

        print("── Rankings ────────────────────────────────────────────────────")
        print(f"{'Rank':<5} {'Builder':<40} {'Score':>8}")
        print("─" * 56)
        for rank, (_, row) in enumerate(df.iterrows(), 1):
            name = str(row[builder_col])
            score = row[score_col]
            flag = " ◀ MAJOR" if any(b in name.lower() for b in MAJOR_BUILDERS) else ""
            print(f"{rank:<5} {name:<40} {score:>7.1f}%{flag}")

        print("\n── Key stats ───────────────────────────────────────────────────")
        print(f"  Highest score:  {df[score_col].max():.1f}% — {df.loc[df[score_col].idxmax(), builder_col]}")
        print(f"  Lowest score:   {df[score_col].min():.1f}% — {df.loc[df[score_col].idxmin(), builder_col]}")
        print(f"  Average score:  {df[score_col].mean():.1f}%")
        print(f"  Spread (max-min): {df[score_col].max() - df[score_col].min():.1f} percentage points")
        print(f"  Builders listed: {len(df)}")

        # Major builders only
        major = df[df[builder_col].str.lower().apply(
            lambda x: any(b in x for b in MAJOR_BUILDERS)
        )]
        if not major.empty:
            print(f"\n── Major builders only ─────────────────────────────────────────")
            for _, row in major.iterrows():
                print(f"  {row[builder_col]:<40} {row[score_col]:>7.1f}%")

    else:
        print("── Raw data (no score column detected) ─────────────────────────")
        print(df.to_string(index=False))

    print("\n────────────────────────────────────────────────────────────────")
    print("  Tip: copy the rankings table above into your Reddit post!")
    print("────────────────────────────────────────────────────────────────\n")


def main():
    print("\n── HBF Data Analyser ───────────────────────────────────────────\n")
    print("  Loading data...")
    df = load_data(INPUT_FILE)
    analyse(df)


if __name__ == "__main__":
    main()
