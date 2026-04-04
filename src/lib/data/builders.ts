export interface Builder {
	slug: string;
	name: string;
	shortName: string;
	avgScore: number;
	trend: string;
	hbfStar: number;
	homesPerYear: string;
	description: string;
	quarterlyScores: (number | null)[];
}

export const QUARTERS = [
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

export const builders: Builder[] = [
	{
		slug: 'barratt-developments',
		name: 'Barratt Developments',
		shortName: 'Barratt',
		avgScore: 94.2,
		trend: 'stable',
		hbfStar: 5,
		homesPerYear: '~19,000',
		description:
			"The UK's largest housebuilder by volume, formed after the 2024 merger with Redrow. Consistently holds HBF 5-star status with satisfaction scores above 94%.",
		quarterlyScores: [
			0.94, 0.945, 0.942, 0.94, 0.94, 0.954, 0.952, 0.953, 0.937, 0.935, 0.936, 0.949, 0.951,
			0.952, 0.975, 0.96, 0.976, 0.964, 0.97
		]
	},
	{
		slug: 'taylor-wimpey',
		name: 'Taylor Wimpey',
		shortName: 'Taylor Wimpey',
		avgScore: 92.6,
		trend: 'improving',
		hbfStar: 5,
		homesPerYear: '~14,000',
		description:
			"One of the UK's largest housebuilders with a national presence. Satisfaction scores have steadily improved since 2022, reaching 95.7% in 2025.",
		quarterlyScores: [
			null, null, null, null, 0.908, 0.91, 0.913, 0.906, 0.924, 0.906, 0.909, 0.911, 0.914, 0.909,
			0.914, 0.909, 0.959, 0.957, 0.957
		]
	},
	{
		slug: 'persimmon-homes',
		name: 'Persimmon Homes',
		shortName: 'Persimmon',
		avgScore: 92.8,
		trend: 'recovering',
		hbfStar: 5,
		homesPerYear: '~14,000',
		description:
			"Persimmon suffered the dataset's most dramatic collapse when scores fell to 81.4% in Q3 2022. A sustained improvement programme has brought them back to ~95% by 2025.",
		quarterlyScores: [
			0.908, 0.937, 0.916, 0.92, 0.913, 0.943, 0.814, 0.913, 0.904, 0.905, 0.918, 0.911, 0.94,
			0.941, 0.909, 0.926, 0.952, 0.957, 0.954
		]
	},
	{
		slug: 'bellway-homes',
		name: 'Bellway Homes',
		shortName: 'Bellway',
		avgScore: 93.5,
		trend: 'stable',
		hbfStar: 5,
		homesPerYear: '~10,000',
		description:
			'Bellway consistently performs above the major-builder average. A reliable mid-market performer with satisfaction scores typically between 93–96%.',
		quarterlyScores: [
			0.938, 0.943, 0.936, 0.93, 0.931, 0.909, 0.923, 0.94, 0.935, 0.923, 0.946, 0.956, 0.956,
			0.938, 0.938, 0.96, 0.957, 0.958, 0.963
		]
	},
	{
		slug: 'bloor-homes',
		name: 'Bloor Homes',
		shortName: 'Bloor',
		avgScore: 96.4,
		trend: 'stable',
		hbfStar: 5,
		homesPerYear: '~3,000',
		description:
			'The best-performing major builder in the dataset. Bloor Homes is a family-owned business that consistently scores above 95% — yet remains largely unknown to buyers.',
		quarterlyScores: [
			0.948, 0.944, 0.952, 0.953, 0.956, 0.954, 0.968, 0.946, 0.946, 0.953, 0.953, 0.964, 0.975,
			0.96, 0.951, 0.958, 0.96, 0.96, 0.963
		]
	},
	{
		slug: 'keepmoat',
		name: 'Keepmoat',
		shortName: 'Keepmoat',
		avgScore: 92.1,
		trend: 'stable',
		hbfStar: 5,
		homesPerYear: '~4,000',
		description:
			'Keepmoat focuses on affordable homes across the North of England and Midlands. Scores are generally solid but showed volatility in 2022.',
		quarterlyScores: [
			0.928, 0.928, 0.928, 0.91, 0.928, 0.843, 0.906, 0.908, 0.906, 0.945, 0.9, 0.902, 0.943,
			0.954, 0.943, 0.944, 0.963, 0.967, 0.947
		]
	},
	{
		slug: 'crest-nicholson',
		name: 'Crest Nicholson',
		shortName: 'Crest Nicholson',
		avgScore: 90.9,
		trend: 'improving',
		hbfStar: 4,
		homesPerYear: '~2,000',
		description:
			"The dataset's biggest turnaround story. After falling to 86.5% in mid-2022, Crest Nicholson recovered strongly to above 97% by 2024 — the most dramatic improvement of any major builder.",
		quarterlyScores: [
			0.93, 0.925, 0.913, 0.89, 0.925, 0.899, 0.882, 0.939, 0.873, 0.865, 0.899, 0.903, 0.968,
			0.952, 0.968, 0.95, 0.975, 0.975, 0.963
		]
	},
	{
		slug: 'miller-homes',
		name: 'Miller Homes',
		shortName: 'Miller',
		avgScore: 92.7,
		trend: 'stable',
		hbfStar: 5,
		homesPerYear: '~3,500',
		description:
			'Miller Homes is a Scotland-based builder with a growing UK-wide presence. Consistently solid scores with minimal volatility across the 19-quarter dataset.',
		quarterlyScores: [
			0.934, 0.931, 0.923, 0.905, 0.934, 0.924, 0.915, 0.925, 0.929, 0.931, 0.927, 0.909, 0.927,
			0.931, 0.931, 0.931, 0.962, 0.96, 0.952
		]
	},
	{
		slug: 'cala-homes',
		name: 'CALA Homes',
		shortName: 'CALA',
		avgScore: 95.0,
		trend: 'stable',
		hbfStar: 5,
		homesPerYear: '~3,000',
		description:
			'CALA Homes focuses on premium new builds, particularly in Scotland and the South East. Consistently among the top performers with scores above 95%.',
		quarterlyScores: [
			0.95, 0.948, 0.945, 0.95, 0.95, 0.954, 0.936, 0.954, 0.932, 0.944, 0.95, 0.974, 0.978,
			0.954, 0.959, 0.961, 0.978, 0.964, 0.964
		]
	},
	{
		slug: 'berkeley-group',
		name: 'Berkeley Group',
		shortName: 'Berkeley',
		avgScore: 95.8,
		trend: 'stable',
		hbfStar: 5,
		homesPerYear: '~5,000',
		description:
			'Berkeley Group focuses on complex urban regeneration projects in London and the South East. One of the strongest performers in the dataset.',
		quarterlyScores: [
			null, null, null, null, null, null, null, null, null, null, null, null, 0.96, 0.958, 0.955,
			0.959, 0.96, 0.958, 0.96
		]
	},
	{
		slug: 'vistry-group',
		name: 'Vistry Group',
		shortName: 'Vistry',
		avgScore: 93.1,
		trend: 'improving',
		hbfStar: 5,
		homesPerYear: '~17,000',
		description:
			"Formed from the merger of Bovis Homes and Galliford Try Partnerships, Vistry has grown into one of the UK's largest builders. Scores have improved steadily.",
		quarterlyScores: [
			null, null, null, null, null, null, null, null, 0.92, 0.925, 0.928, 0.932, 0.935, 0.93,
			0.933, 0.938, 0.942, 0.945, 0.948
		]
	},
	{
		slug: 'bovis-homes',
		name: 'Bovis Homes',
		shortName: 'Bovis',
		avgScore: 91.4,
		trend: 'stable',
		hbfStar: 5,
		homesPerYear: '~3,000',
		description:
			'Now operating under the Vistry Group umbrella, Bovis Homes maintains stable satisfaction scores around 91–92%.',
		quarterlyScores: [
			0.905, 0.91, 0.908, 0.912, 0.915, 0.91, 0.908, 0.913, 0.914, 0.912, 0.916, 0.918, 0.92,
			0.916, 0.914, 0.918, 0.92, 0.918, 0.916
		]
	}
];

export function getBuilderBySlug(slug: string): Builder | undefined {
	return builders.find((b) => b.slug === slug);
}

export function scoreColour(score: number): string {
	if (score >= 95) return '#3D7A52';
	if (score >= 90) return '#E8960C';
	return '#E03A2F';
}

export function scoreClass(score: number): string {
	if (score >= 95) return 'score-high';
	if (score >= 90) return 'score-mid';
	return 'score-low';
}

export function scoreBadgeStyle(score: number): string {
	if (score >= 95) return 'background:#EBF4EE;color:#2A5A3A';
	if (score >= 90) return 'background:#FEF3D7;color:#B87208';
	return 'background:#FDEEED;color:#B02820';
}

export const BUILDER_SCORES: Record<string, { score: number; trend: string; hbfStar: number }> =
	Object.fromEntries(
		builders.map((b) => [b.name, { score: b.avgScore, trend: b.trend, hbfStar: b.hbfStar }])
	);
