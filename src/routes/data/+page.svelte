<script lang="ts">
	import { onMount } from 'svelte';

	const QUARTERS = [
		'Q1 2021',
		'Q2 2021',
		'Q3 2021',
		'Q4 2021',
		'Q1 2022',
		'Q2 2022',
		'Q3 2022',
		'Q4 2022',
		'Q1 2023',
		'Q2 2023',
		'Q3 2023',
		'Q4 2023',
		'Q1 2024',
		'Q2 2024',
		'Q3 2024',
		'Q4 2024',
		'Q1 2025',
		'Q2 2025',
		'Q3 2025'
	];

	const RAW_BUILDERS: Record<string, (number | null)[]> = {
		'Barratt Developments': [
			0.94, 0.945, 0.942, 0.94, 0.94, 0.954, 0.952, 0.953, 0.937, 0.935, 0.936, 0.949, 0.951, 0.952,
			0.975, 0.96, 0.976, 0.964, 0.97
		],
		'Taylor Wimpey': [
			null,
			null,
			null,
			null,
			0.908,
			0.91,
			0.913,
			0.906,
			0.924,
			0.906,
			0.909,
			0.911,
			0.914,
			0.909,
			0.914,
			0.909,
			0.959,
			0.957,
			0.957
		],
		'Persimmon Homes': [
			0.908, 0.937, 0.916, 0.92, 0.913, 0.943, 0.814, 0.913, 0.904, 0.905, 0.918, 0.911, 0.94,
			0.941, 0.909, 0.926, 0.952, 0.957, 0.954
		],
		'Bellway Homes': [
			0.938, 0.943, 0.936, 0.93, 0.931, 0.909, 0.923, 0.94, 0.935, 0.923, 0.946, 0.956, 0.956,
			0.938, 0.938, 0.96, 0.957, 0.958, 0.963
		],
		'Bloor Homes': [
			0.948, 0.944, 0.952, 0.953, 0.956, 0.954, 0.968, 0.946, 0.946, 0.953, 0.953, 0.964, 0.975,
			0.96, 0.951, 0.958, 0.96, 0.96, 0.963
		],
		'Redrow Homes': [
			0.928,
			0.976,
			0.928,
			0.924,
			0.928,
			0.933,
			0.916,
			0.969,
			0.969,
			0.976,
			0.921,
			0.935,
			null,
			null,
			null,
			null,
			null,
			null,
			null
		],
		Keepmoat: [
			0.928, 0.928, 0.928, 0.91, 0.928, 0.843, 0.906, 0.908, 0.906, 0.945, 0.9, 0.902, 0.943, 0.954,
			0.943, 0.944, 0.963, 0.967, 0.947
		],
		'Crest Nicholson': [
			0.93, 0.925, 0.913, 0.89, 0.925, 0.899, 0.882, 0.939, 0.873, 0.865, 0.899, 0.903, 0.968,
			0.952, 0.968, 0.95, 0.975, 0.975, 0.963
		],
		'Miller Homes': [
			0.934, 0.931, 0.923, 0.905, 0.934, 0.924, 0.915, 0.925, 0.929, 0.931, 0.927, 0.909, 0.927,
			0.931, 0.931, 0.931, 0.962, 0.96, 0.952
		],
		'CALA Homes': [
			0.95, 0.948, 0.945, 0.95, 0.95, 0.954, 0.936, 0.954, 0.932, 0.944, 0.95, 0.974, 0.978, 0.954,
			0.959, 0.961, 0.978, 0.964, 0.964
		]
	};

	const COLOURS = [
		'#3D7A52',
		'#E03A2F',
		'#2A5A3A',
		'#B02820',
		'#6BAF87',
		'#F5A59A',
		'#1a5c38',
		'#c84b40',
		'#4da675',
		'#ff7c70'
	];

	let canvas: HTMLCanvasElement;
	let chart: any = null;
	let activeView = $state('trend');
	let chartNote = $state(
		'Showing 10 major builders. Scores represent the percentage of buyers who would recommend their builder. Source: Home Builders Federation (HBF) Customer Satisfaction Survey.'
	);

	const FORMSPREE = 'https://formspree.io/f/mzdjypjg';
	let email = $state('');
	let sending = $state(false);
	let success = $state(false);
	let inputError = $state(false);

	function avg(arr: (number | null)[]): number | null {
		const v = arr.filter((x): x is number => x !== null);
		return v.length ? v.reduce((a, b) => a + b, 0) / v.length : null;
	}

	function pct(v: number | null): number | null {
		return v !== null ? Math.round(v * 1000) / 10 : null;
	}

	function shortName(b: string): string {
		return b.replace(' Developments', '').replace(' Homes', '');
	}

	async function showChart(view: string) {
		activeView = view;
		const { Chart } = await import('chart.js/auto');
		const ctx = canvas.getContext('2d')!;
		if (chart) chart.destroy();

		const builderNames = Object.keys(RAW_BUILDERS);

		if (view === 'trend') {
			chartNote =
				'Trend over time — % of buyers who would recommend their builder. Q1 2021 – Q3 2025. Gaps indicate quarters with insufficient data.';
			const datasets = builderNames.map((b, i) => ({
				label: shortName(b),
				data: RAW_BUILDERS[b].map(pct),
				borderColor: COLOURS[i],
				backgroundColor: COLOURS[i] + '18',
				borderWidth: 2,
				pointRadius: 3,
				pointHoverRadius: 5,
				tension: 0.3,
				spanGaps: true
			}));
			chart = new Chart(ctx, {
				type: 'line',
				data: { labels: QUARTERS, datasets },
				options: {
					responsive: true,
					interaction: { mode: 'index', intersect: false },
					plugins: {
						legend: {
							position: 'bottom',
							labels: { font: { family: 'Nunito', size: 11 }, boxWidth: 12, padding: 10 }
						},
						tooltip: {
							callbacks: {
								label: (c) =>
									` ${c.dataset.label}: ${c.parsed.y !== null ? c.parsed.y.toFixed(1) + '%' : 'n/a'}`
							}
						}
					},
					scales: {
						y: {
							min: 78,
							max: 100,
							ticks: { callback: (v) => v + '%', font: { family: 'Nunito', size: 11 } },
							grid: { color: 'rgba(0,0,0,0.06)' }
						},
						x: {
							ticks: { font: { family: 'Nunito', size: 10 }, maxRotation: 45 },
							grid: { display: false }
						}
					}
				}
			});
		} else if (view === 'ranking') {
			chartNote =
				'Average satisfaction score across all available quarters. Only builders with 4+ data points included.';
			const avgs = builderNames
				.map((b) => ({ b: shortName(b), v: pct(avg(RAW_BUILDERS[b])) }))
				.filter((x): x is { b: string; v: number } => x.v !== null)
				.sort((a, b) => b.v - a.v);
			chart = new Chart(ctx, {
				type: 'bar',
				data: {
					labels: avgs.map((x) => x.b),
					datasets: [
						{
							label: 'Avg score',
							data: avgs.map((x) => x.v),
							backgroundColor: avgs.map((_, i) => COLOURS[i % COLOURS.length]),
							borderRadius: 8,
							borderSkipped: false
						}
					]
				},
				options: {
					indexAxis: 'y',
					responsive: true,
					plugins: {
						legend: { display: false },
						tooltip: { callbacks: { label: (c) => ` ${c.parsed.x.toFixed(1)}%` } }
					},
					scales: {
						x: {
							min: 88,
							max: 100,
							ticks: { callback: (v) => v + '%', font: { family: 'Nunito', size: 11 } },
							grid: { color: 'rgba(0,0,0,0.06)' }
						},
						y: {
							ticks: { font: { family: 'Nunito', size: 12, weight: 700 } },
							grid: { display: false }
						}
					}
				}
			});
		} else if (view === 'latest') {
			chartNote = 'Most recent available quarter score for each builder.';
			const latest = builderNames
				.map((b) => {
					const arr = RAW_BUILDERS[b];
					const revIdx = [...arr].reverse().findIndex((x) => x !== null);
					const v = revIdx !== -1 ? arr[arr.length - 1 - revIdx] : null;
					return { b: shortName(b), v: pct(v) };
				})
				.filter((x): x is { b: string; v: number } => x.v !== null)
				.sort((a, b) => b.v - a.v);
			chart = new Chart(ctx, {
				type: 'bar',
				data: {
					labels: latest.map((x) => x.b),
					datasets: [
						{
							label: 'Latest score',
							data: latest.map((x) => x.v),
							backgroundColor: latest.map((_, i) => COLOURS[i % COLOURS.length]),
							borderRadius: 8,
							borderSkipped: false
						}
					]
				},
				options: {
					indexAxis: 'y',
					responsive: true,
					plugins: {
						legend: { display: false },
						tooltip: { callbacks: { label: (c) => ` ${c.parsed.x.toFixed(1)}%` } }
					},
					scales: {
						x: {
							min: 88,
							max: 100,
							ticks: { callback: (v) => v + '%', font: { family: 'Nunito', size: 11 } },
							grid: { color: 'rgba(0,0,0,0.06)' }
						},
						y: {
							ticks: { font: { family: 'Nunito', size: 12, weight: 700 } },
							grid: { display: false }
						}
					}
				}
			});
		}
	}

	async function handleSignup() {
		const valid = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.trim());
		if (!valid) {
			inputError = true;
			return;
		}
		inputError = false;
		sending = true;
		try {
			const res = await fetch(FORMSPREE, {
				method: 'POST',
				headers: { Accept: 'application/json', 'Content-Type': 'application/json' },
				body: JSON.stringify({ email: email.trim() })
			});
			if (res.ok) success = true;
			else alert('Something went wrong — please try again.');
		} catch {
			alert('Network error — please try again.');
		} finally {
			sending = false;
		}
	}

	onMount(() => showChart('trend'));
</script>

<svelte:head>
	<title>HBF Satisfaction Data — WhoBuilt</title>
	<meta
		name="description"
		content="Interactive chart showing HBF customer satisfaction scores for major UK housebuilders from Q1 2021 to Q3 2025."
	/>
</svelte:head>

<!-- Hero band -->
<div style="background: var(--color-sage-light); padding: 2rem 1.5rem;">
	<div style="max-width: 900px; margin: 0 auto;">
		<div
			class="mb-3 inline-flex items-center gap-1.5 rounded-full px-3 py-1 text-[11px] font-extrabold tracking-[0.06em] text-white uppercase"
			style="background: var(--color-sage);"
		>
			<svg width="12" height="12" viewBox="0 0 12 12" fill="none">
				<circle cx="6" cy="6" r="5" stroke="#fff" stroke-width="1.5" />
				<path d="M6 4v3M6 8.5v.5" stroke="#fff" stroke-width="1.5" stroke-linecap="round" />
			</svg>
			19 quarters · 10 major builders
		</div>
		<h1
			class="mb-2 font-serif text-[clamp(22px,4vw,36px)] leading-[1.2] font-bold"
			style="color: var(--color-ink);"
		>
			Which builder do buyers actually <em style="color: var(--color-red-dark);">recommend</em>?
		</h1>
		<p class="max-w-[620px] text-sm leading-relaxed font-semibold" style="color: #3a5040;">
			HBF "Would you recommend your builder?" survey results for major UK housebuilders, Q1 2021 to
			Q3 2025. The gap between best and worst is bigger than the industry wants you to know.
		</p>
	</div>
</div>

<!-- Stats strip -->
<div class="page" style="padding-top: 1.25rem; padding-bottom: 0;">
	<div class="mb-4 grid gap-3" style="grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));">
		<div class="stat-card">
			<div class="stat-num accent">19</div>
			<div class="stat-label">Quarters of data analysed</div>
		</div>
		<div class="stat-card">
			<div class="stat-num">10</div>
			<div class="stat-label">Major builders tracked</div>
		</div>
		<div class="stat-card">
			<div class="stat-num accent">96.4%</div>
			<div class="stat-label">Highest avg — Bloor Homes</div>
		</div>
		<div class="stat-card">
			<div class="stat-num">90.9%</div>
			<div class="stat-label">Lowest avg — Crest Nicholson</div>
		</div>
		<div class="stat-card">
			<div class="stat-num">5.5pp</div>
			<div class="stat-label">Spread between best &amp; worst</div>
		</div>
	</div>

	<!-- Chart -->
	<div class="card mb-4">
		<div class="mb-4">
			<div class="text-[15px] font-extrabold" style="color: var(--color-ink);">
				Housebuilder satisfaction scores
			</div>
			<div class="text-[12px] font-semibold" style="color: var(--color-muted);">
				% of buyers who would recommend their builder to a friend
			</div>
		</div>

		<div class="mb-4 flex flex-wrap gap-1.5">
			{#each [['trend', 'Trend over time'], ['ranking', 'Overall ranking'], ['latest', 'Latest quarter']] as [view, label] (label)}
				<button
					class="tab"
					class:active={activeView === view}
					onclick={() => showChart(view)}
					style="padding:6px 14px;font-size:12px;font-weight:700;border-radius:100px;border:1.5px solid var(--color-border);background:{activeView ===
					view
						? 'var(--color-sage)'
						: 'var(--color-bg)'};color:{activeView === view
						? '#fff'
						: 'var(--color-muted)'};cursor:pointer;font-family:'Nunito',sans-serif;transition:all 0.15s;"
				>
					{label}
				</button>
			{/each}
		</div>

		<canvas bind:this={canvas}></canvas>

		<p
			class="mt-3 border-t pt-3 text-[11px] font-semibold"
			style="color:var(--color-muted);border-color:var(--color-border);"
		>
			{chartNote}
		</p>
	</div>

	<!-- Insight cards -->
	<div class="section-title">What the data tells us</div>
	<div class="mb-6 grid gap-3" style="grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));">
		{#each [{ label: 'Consistently best', title: 'Bloor Homes & CALA Homes', body: 'Both maintain scores above 95% across nearly every quarter — far above the major-builder average.' }, { label: 'Most improved', title: 'Crest Nicholson', body: 'Dropped sharply to 86.5% in Q3 2022, then recovered strongly to above 97% by 2024 — the biggest turnaround in the dataset.' }, { label: 'Notable dip', title: 'Persimmon Homes — Q3 2022', body: 'Fell to 81.4% in Q3 2022, the lowest single-quarter score of any major builder. Recovered to ~95% by 2025.' }, { label: 'The industry problem', title: 'Surveys taken 8 weeks after completion', body: 'The HBF survey is sent before most defects appear. NHBC\'s own 9-month survey scores run 5–10% lower — the "honeymoon effect."' }] as insight (insight)}
			<div class="card" style="border-radius: var(--radius-sm);">
				<div
					class="mb-1.5 text-[10px] font-extrabold tracking-[0.08em] uppercase"
					style="color: var(--color-sage);"
				>
					{insight.label}
				</div>
				<div class="text-[13px] leading-snug font-bold" style="color: var(--color-ink);">
					{insight.title}
				</div>
				<div
					class="mt-0.5 text-[12px] leading-relaxed font-semibold"
					style="color: var(--color-muted);"
				>
					{insight.body}
				</div>
			</div>
		{/each}
	</div>

	<!-- CTA -->
	<div class="cta-block">
		<div class="section-title">Want the full picture before you buy?</div>
		<p class="cta-sub">
			WhoBuilt is building the UK's first independent housebuilder comparison service. Join the
			waitlist to get access at launch.
		</p>
		{#if !success}
			<div class="form-wrap">
				<input
					type="email"
					bind:value={email}
					class:error={inputError}
					placeholder="your@email.com"
					autocomplete="email"
					onkeydown={(e) => e.key === 'Enter' && handleSignup()}
				/>
				<button onclick={handleSignup} disabled={sending}>
					{sending ? 'Sending…' : 'Join waitlist'}
				</button>
			</div>
		{:else}
			<p class="pt-2 text-[15px] font-extrabold" style="color: var(--color-sage);">
				You're on the list — we'll be in touch before launch.
			</p>
		{/if}
	</div>

	<footer class="footer">
		<div class="footer-logo">WhoBuilt</div>
		<div class="footer-copy">
			© 2026 WhoBuilt Ltd · whobuilt.org · Data source: HBF Customer Satisfaction Survey
		</div>
	</footer>
</div>
