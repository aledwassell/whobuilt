<script lang="ts">
	import { builders, scoreBadgeStyle, scoreClass } from '$lib/data/builders';

	const sorted = [...builders].sort((a, b) => b.avgScore - a.avgScore);

	const trendLabel: Record<string, string> = {
		stable: 'Stable',
		improving: 'Improving',
		recovering: 'Recovering'
	};

	const trendColour: Record<string, string> = {
		stable: 'color:#6b7a6f',
		improving: 'color:#2A5A3A',
		recovering: 'color:#B87208'
	};
</script>

<svelte:head>
	<title>UK Housebuilder Comparison — WhoBuilt</title>
	<meta
		name="description"
		content="Compare major UK housebuilders by customer satisfaction score. Independent data from the HBF survey, Q1 2021 to Q3 2025."
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
			{builders.length} builders · HBF satisfaction data
		</div>
		<h1
			class="mb-2 font-serif text-[clamp(22px,4vw,36px)] font-bold leading-[1.2]"
			style="color: var(--color-ink);"
		>
			Compare UK housebuilders
		</h1>
		<p class="max-w-[620px] text-sm font-semibold leading-relaxed" style="color: #3a5040;">
			Ranked by average customer satisfaction score from the HBF survey (Q1 2021 – Q3 2025). Click
			any builder to see their full score history.
		</p>
	</div>
</div>

<div class="page" style="padding-top: 1.5rem;">
	<!-- Builder list -->
	<div class="mb-6 flex flex-col gap-3">
		{#each sorted as builder, i (builder.slug)}
			<a
				href="/builders/{builder.slug}"
				class="card flex items-center gap-4 no-underline transition-all duration-150 hover:-translate-y-0.5 hover:border-[var(--color-sage)]"
				style="display: flex; text-decoration: none;"
			>
				<!-- Rank -->
				<div
					class="flex h-9 w-9 flex-shrink-0 items-center justify-center rounded-full text-[13px] font-black"
					style="background: var(--color-sage-light); color: var(--color-sage-dark);"
				>
					{i + 1}
				</div>

				<!-- Name + meta -->
				<div class="min-w-0 flex-1">
					<div class="text-[15px] font-extrabold" style="color: var(--color-ink);">
						{builder.name}
					</div>
					<div class="text-[12px] font-semibold" style="color: var(--color-muted);">
						{builder.homesPerYear} homes/yr ·
						<span style={trendColour[builder.trend]}>{trendLabel[builder.trend]}</span>
					</div>
				</div>

				<!-- HBF stars -->
				<div class="hidden flex-shrink-0 flex-col items-end sm:flex">
					<div class="mb-0.5 flex gap-0.5">
						{#each Array(5) as _, s (s)}
							<svg width="12" height="12" viewBox="0 0 12 12" fill="none">
								<path
									d="M6 1.5l1.2 2.8L10 4.6l-2 2 .5 3L6 8.2 3.5 9.6l.5-3-2-2 2.8-.3z"
									fill={s < builder.hbfStar ? '#E8960C' : '#D8E8DE'}
								/>
							</svg>
						{/each}
					</div>
					<div class="text-[10px] font-semibold" style="color: var(--color-muted);">HBF rating</div>
				</div>

				<!-- Score badge -->
				<div class="score-badge {scoreClass(builder.avgScore)} flex-shrink-0">
					{builder.avgScore.toFixed(1)}%
				</div>

				<!-- Chevron -->
				<svg
					width="16"
					height="16"
					viewBox="0 0 16 16"
					fill="none"
					class="flex-shrink-0 opacity-40"
				>
					<path
						d="M6 3l5 5-5 5"
						stroke="currentColor"
						stroke-width="2"
						stroke-linecap="round"
						stroke-linejoin="round"
					/>
				</svg>
			</a>
		{/each}
	</div>

	<!-- Caveat -->
	<p class="mb-8 text-[11px] font-semibold" style="color: var(--color-muted);">
		Scores from the HBF Customer Satisfaction Survey — "Would you recommend your builder to a
		friend?". Sent 8 weeks post-completion. NHBC 9-month scores typically run 5–10% lower.
	</p>

	<!-- CTA -->
	<div class="manifesto">
		<blockquote>
			"These scores are a starting point, not the full picture. HBF surveys are taken before most
			defects appear. WhoBuilt will layer in NHBC warranty data, resident reviews, and after-sales
			tracking."
		</blockquote>
		<cite>— The WhoBuilt methodology</cite>
	</div>

	<footer class="footer">
		<div class="footer-logo">WhoBuilt</div>
		<div class="footer-copy">
			© 2026 WhoBuilt Ltd · Data source: HBF Customer Satisfaction Survey
		</div>
	</footer>
</div>
