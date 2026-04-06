<script lang="ts">
	import { onMount } from 'svelte';
	import { QUARTERS, scoreClass, scoreBadgeStyle } from '$lib/data/builders';

	let { data } = $props();
	const builder = $derived(data.builder);

	const trendLabel: Record<string, string> = {
		stable: 'Stable',
		improving: 'Improving ↑',
		recovering: 'Recovering ↑'
	};

	const trendStyle: Record<string, string> = {
		stable: 'background:#f0f0f0;color:#4a5a4e',
		improving: 'background:#EBF4EE;color:#2A5A3A',
		recovering: 'background:#FEF3D7;color:#B87208'
	};

	// Quarterly data as percentages (null-safe)
	const pctScores = $derived(
		builder.quarterlyScores.map((v) => (v !== null ? Math.round(v * 1000) / 10 : null))
	);

	// Min/max for context
	const nonNull = $derived(pctScores.filter((v): v is number => v !== null));
	const minScore = $derived(Math.min(...nonNull));
	const maxScore = $derived(Math.max(...nonNull));
	const latestScore = $derived([...pctScores].reverse().find((v) => v !== null) ?? null);

	const canonicalUrl = $derived(`https://whobuilt.org/builders/${builder.slug}`);
	const metaTitle = $derived(`${builder.name} — HBF Satisfaction Scores · WhoBuilt`);
	const metaDescription = $derived(
		`${builder.description} Average HBF score: ${builder.avgScore.toFixed(1)}% (Q1 2021–Q3 2025).`
	);

	let canvas: HTMLCanvasElement;
	let chart: any = null;

	onMount(async () => {
		const { Chart } = await import('chart.js/auto');
		const ctx = canvas.getContext('2d')!;

		const colour =
			builder.avgScore >= 95 ? '#3D7A52' : builder.avgScore >= 90 ? '#E8960C' : '#E03A2F';

		chart = new Chart(ctx, {
			type: 'line',
			data: {
				labels: QUARTERS,
				datasets: [
					{
						label: builder.shortName,
						data: pctScores,
						borderColor: colour,
						backgroundColor: colour + '18',
						borderWidth: 2.5,
						pointRadius: 4,
						pointHoverRadius: 6,
						tension: 0.3,
						spanGaps: true,
						fill: true
					}
				]
			},
			options: {
				responsive: true,
				interaction: { mode: 'index', intersect: false },
				plugins: {
					legend: { display: false },
					tooltip: {
						callbacks: {
							label: (c) => ` ${c.parsed.y !== null ? c.parsed.y.toFixed(1) + '%' : 'No data'}`
						}
					}
				},
				scales: {
					y: {
						min: Math.max(75, Math.floor(minScore) - 3),
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

		return () => chart?.destroy();
	});
</script>

<svelte:head>
	<title>{metaTitle}</title>
	<meta name="description" content={metaDescription} />
	<link rel="canonical" href={canonicalUrl} />

	<!-- Open Graph -->
	<meta property="og:type" content="website" />
	<meta property="og:site_name" content="WhoBuilt" />
	<meta property="og:url" content={canonicalUrl} />
	<meta property="og:title" content={metaTitle} />
	<meta property="og:description" content={metaDescription} />

	<!-- Twitter Card -->
	<meta name="twitter:card" content="summary" />
	<meta name="twitter:title" content={metaTitle} />
	<meta name="twitter:description" content={metaDescription} />
</svelte:head>

<!-- Breadcrumb -->
<div class="page" style="padding-bottom: 0; padding-top: 1rem;">
	<div
		class="mb-4 flex items-center gap-1.5 text-[12px] font-semibold"
		style="color: var(--color-muted);"
	>
		<a href="/builders" style="color: var(--color-sage); text-decoration: none;">Builders</a>
		<span>›</span>
		<span>{builder.name}</span>
	</div>
</div>

<!-- Hero band -->
<div style="background: var(--color-sage-light); padding: 2rem 1.5rem; margin-bottom: 0;">
	<div style="max-width: 900px; margin: 0 auto;">
		<div class="flex flex-wrap items-start justify-between gap-4">
			<div>
				<h1
					class="mb-2 font-serif text-[clamp(24px,4vw,40px)] leading-[1.2] font-bold"
					style="color: var(--color-ink);"
				>
					{builder.name}
				</h1>
				<div class="flex flex-wrap items-center gap-2">
					<span
						class="rounded-full px-2.5 py-1 text-[11px] font-extrabold"
						style={trendStyle[builder.trend]}
					>
						{trendLabel[builder.trend]}
					</span>
					<span class="text-[12px] font-semibold" style="color: var(--color-muted);">
						{builder.homesPerYear} homes/yr
					</span>
					<!-- HBF stars -->
					<div class="flex gap-0.5">
						{#each Array(5) as _, s (s)}
							<svg width="14" height="14" viewBox="0 0 12 12" fill="none">
								<path
									d="M6 1.5l1.2 2.8L10 4.6l-2 2 .5 3L6 8.2 3.5 9.6l.5-3-2-2 2.8-.3z"
									fill={s < builder.hbfStar ? '#E8960C' : '#c4dfd0'}
								/>
							</svg>
						{/each}
						<span class="ml-1 text-[11px] font-semibold" style="color: var(--color-muted);"
							>HBF</span
						>
					</div>
				</div>
			</div>
			<!-- Score -->
			<div class="text-right">
				<div
					class="font-serif text-[clamp(36px,6vw,56px)] leading-none font-bold"
					style="color: var(--color-sage-dark);"
				>
					{builder.avgScore.toFixed(1)}%
				</div>
				<div class="text-[12px] font-semibold" style="color: var(--color-muted);">avg score</div>
			</div>
		</div>
		<p class="mt-4 max-w-[640px] text-sm leading-relaxed font-semibold" style="color: #3a5040;">
			{builder.description}
		</p>
	</div>
</div>

<div class="page" style="padding-top: 1.5rem;">
	<!-- Stat strip -->
	<div class="mb-5 grid gap-3" style="grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));">
		<div class="stat-card">
			<div class="stat-num">{builder.avgScore.toFixed(1)}%</div>
			<div class="stat-label">Average score</div>
		</div>
		{#if latestScore !== null}
			<div class="stat-card">
				<div class="stat-num accent">{latestScore.toFixed(1)}%</div>
				<div class="stat-label">Latest quarter</div>
			</div>
		{/if}
		<div class="stat-card">
			<div class="stat-num">{maxScore.toFixed(1)}%</div>
			<div class="stat-label">Best quarter</div>
		</div>
		<div class="stat-card">
			<div class="stat-num">{minScore.toFixed(1)}%</div>
			<div class="stat-label">Worst quarter</div>
		</div>
	</div>

	<!-- Chart -->
	<div class="card mb-5">
		<div class="mb-4">
			<div class="text-[15px] font-extrabold" style="color: var(--color-ink);">
				Satisfaction score over time
			</div>
			<div class="text-[12px] font-semibold" style="color: var(--color-muted);">
				% of buyers who would recommend {builder.shortName} to a friend · Q1 2021 – Q3 2025
			</div>
		</div>
		<canvas bind:this={canvas}></canvas>
		<p
			class="mt-3 border-t pt-3 text-[11px] font-semibold"
			style="color:var(--color-muted);border-color:var(--color-border);"
		>
			Source: HBF Customer Satisfaction Survey. Gaps indicate quarters with insufficient data.
		</p>
	</div>

	<!-- Quarterly table -->
	<div class="card mb-6">
		<div class="mb-3 text-[14px] font-extrabold" style="color: var(--color-ink);">
			Quarterly breakdown
		</div>
		<div class="overflow-x-auto">
			<table style="width:100%;border-collapse:collapse;font-family:'Nunito',sans-serif;">
				<tbody>
					{#each QUARTERS as q, i (q)}
						<tr style="border-bottom:1px solid var(--color-border);">
							<td
								style="padding:7px 0;font-size:12px;font-weight:700;color:var(--color-muted);width:90px;"
							>
								{q}
							</td>
							<td style="padding:7px 8px;">
								{#if pctScores[i] !== null}
									<div class="flex items-center gap-2">
										<!-- Bar -->
										<div
											style="height:6px;border-radius:3px;background:var(--color-border);flex:1;max-width:200px;"
										>
											<div
												style="height:6px;border-radius:3px;background:{pctScores[i]! >= 95
													? '#3D7A52'
													: pctScores[i]! >= 90
														? '#E8960C'
														: '#E03A2F'};width:{((pctScores[i]! - 75) / 25) * 100}%"
											></div>
										</div>
										<span class="score-badge {scoreClass(pctScores[i]!)}" style="font-size:12px;">
											{pctScores[i]!.toFixed(1)}%
										</span>
									</div>
								{:else}
									<span style="font-size:12px;font-weight:600;color:var(--color-muted);">—</span>
								{/if}
							</td>
						</tr>
					{/each}
				</tbody>
			</table>
		</div>
	</div>

	<!-- Back link + CTA -->
	<div class="mb-6 flex items-center gap-3">
		<a
			href="/builders"
			class="rounded-full px-4 py-2 text-[13px] font-bold no-underline"
			style="background:var(--color-sage-light);color:var(--color-sage-dark);"
		>
			← All builders
		</a>
		<a
			href="/data"
			class="rounded-full px-4 py-2 text-[13px] font-bold no-underline"
			style="background:var(--color-border);color:var(--color-ink);"
		>
			Compare all builders →
		</a>
	</div>

	<footer class="footer">
		<div class="footer-logo">WhoBuilt</div>
		<div class="footer-copy">
			© 2026 WhoBuilt Ltd · Data source: HBF Customer Satisfaction Survey
		</div>
	</footer>
</div>
