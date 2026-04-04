<script lang="ts">
	import { onMount } from 'svelte';
	import 'leaflet/dist/leaflet.css';
	import { BUILDER_SCORES } from '$lib/data/builders.js';

	interface Development {
		name: string;
		builder: string;
		lat: number;
		lng: number;
		units: number;
		status: string;
		dist?: number;
	}

	const DEVELOPMENTS: Development[] = [
		// London & SE
		{ name: 'Kidbrooke Village', builder: 'Berkeley Group', lat: 51.4635, lng: 0.0294, units: 4700, status: 'Active' },
		{ name: 'Springhead Park', builder: 'Berkeley Group', lat: 51.4418, lng: 0.2978, units: 950, status: 'Active' },
		{ name: 'White City Living', builder: 'Berkeley Group', lat: 51.5115, lng: -0.2241, units: 1800, status: 'Active' },
		{ name: 'Barking Riverside', builder: 'Bellway Homes', lat: 51.5085, lng: 0.1237, units: 1100, status: 'Active' },
		{ name: 'Millbrook Park', builder: 'Barratt Developments', lat: 51.6198, lng: -0.2032, units: 2000, status: 'Active' },
		{ name: 'The Quarry', builder: 'Barratt Developments', lat: 51.3354, lng: -0.2568, units: 580, status: 'Active' },
		{ name: 'Brooklands', builder: 'Taylor Wimpey', lat: 51.3543, lng: -0.4632, units: 2300, status: 'Active' },
		{ name: 'Ebbsfleet Green', builder: 'Taylor Wimpey', lat: 51.442, lng: 0.337, units: 950, status: 'Active' },
		{ name: 'Beaulieu', builder: 'Crest Nicholson', lat: 51.7254, lng: 0.4892, units: 3600, status: 'Active' },
		{ name: 'Arborfield Green', builder: 'Crest Nicholson', lat: 51.3768, lng: -0.9732, units: 3500, status: 'Active' },
		{ name: 'Otterpool Park', builder: 'Vistry Group', lat: 51.0801, lng: 1.0168, units: 800, status: 'Active' },
		// Midlands
		{ name: 'Durranhill Rise', builder: 'Persimmon Homes', lat: 52.4822, lng: -1.8732, units: 420, status: 'Active' },
		{ name: 'Kingswood Heath', builder: 'Persimmon Homes', lat: 52.3812, lng: -1.5643, units: 560, status: 'Active' },
		{ name: 'Whitmore Park', builder: 'Barratt Developments', lat: 52.4431, lng: -1.4832, units: 890, status: 'Active' },
		{ name: 'Priors Hall Park', builder: 'Vistry Group', lat: 52.4765, lng: -0.5874, units: 5100, status: 'Active' },
		{ name: 'Northstowe', builder: 'Taylor Wimpey', lat: 52.2654, lng: 0.0234, units: 10000, status: 'Active' },
		{ name: 'Houlton', builder: 'Crest Nicholson', lat: 52.3998, lng: -1.2432, units: 6200, status: 'Active' },
		{ name: 'Langley Gate', builder: 'Bellway Homes', lat: 52.5432, lng: -2.0876, units: 340, status: 'Active' },
		{ name: 'Keepmoat at Selly Oak', builder: 'Keepmoat', lat: 52.4365, lng: -1.9321, units: 420, status: 'Active' },
		{ name: 'Bloor at Stretton', builder: 'Bloor Homes', lat: 52.8234, lng: -1.5432, units: 280, status: 'Active' },
		// North West
		{ name: 'Lightfoot Green', builder: 'Persimmon Homes', lat: 53.8012, lng: -2.7432, units: 360, status: 'Active' },
		{ name: 'Logwood Mill', builder: 'Bellway Homes', lat: 53.7654, lng: -2.4876, units: 490, status: 'Active' },
		{ name: 'Peel Hall', builder: 'Taylor Wimpey', lat: 53.4012, lng: -2.3421, units: 1200, status: 'Active' },
		{ name: 'Middlewood Locks', builder: 'Vistry Group', lat: 53.4843, lng: -2.2654, units: 2200, status: 'Active' },
		{ name: 'Keepmoat at Bury', builder: 'Keepmoat', lat: 53.5943, lng: -2.2987, units: 310, status: 'Active' },
		{ name: 'Barratt at Altrincham', builder: 'Barratt Developments', lat: 53.3876, lng: -2.3543, units: 245, status: 'Active' },
		{ name: 'Miller at Norden', builder: 'Miller Homes', lat: 53.6234, lng: -2.1765, units: 195, status: 'Active' },
		// Yorkshire
		{ name: 'Derwenthorpe', builder: 'Barratt Developments', lat: 53.9765, lng: -1.0321, units: 540, status: 'Active' },
		{ name: 'Harrogate Gateway', builder: 'Persimmon Homes', lat: 53.9921, lng: -1.5432, units: 320, status: 'Active' },
		{ name: 'Logic Leeds', builder: 'Bellway Homes', lat: 53.8012, lng: -1.5487, units: 410, status: 'Active' },
		{ name: 'Scholars Walk', builder: 'Miller Homes', lat: 53.8987, lng: -1.6543, units: 185, status: 'Active' },
		{ name: 'Taylor Wimpey at Cottingham', builder: 'Taylor Wimpey', lat: 53.7843, lng: -0.4012, units: 290, status: 'Active' },
		{ name: 'Bloor at Brough', builder: 'Bloor Homes', lat: 53.7298, lng: -0.5654, units: 240, status: 'Active' },
		// East England
		{ name: 'Marleigh', builder: 'Barratt Developments', lat: 52.2287, lng: 0.1987, units: 1350, status: 'Active' },
		{ name: 'Great Kneighton', builder: 'Bellway Homes', lat: 52.1765, lng: 0.1123, units: 2000, status: 'Active' },
		{ name: 'Bovis at Peterborough', builder: 'Bovis Homes', lat: 52.5734, lng: -0.2365, units: 380, status: 'Active' },
		{ name: 'CALA at St Neots', builder: 'CALA Homes', lat: 52.2287, lng: -0.2587, units: 290, status: 'Active' },
		// South West
		{ name: 'Cranbrook', builder: 'Taylor Wimpey', lat: 50.7543, lng: -3.4312, units: 6500, status: 'Active' },
		{ name: 'Sherford', builder: 'Vistry Group', lat: 50.3654, lng: -4.0543, units: 5500, status: 'Active' },
		{ name: 'Barratt at Bristol', builder: 'Barratt Developments', lat: 51.4543, lng: -2.5987, units: 480, status: 'Active' },
		{ name: 'Bloor at Taunton', builder: 'Bloor Homes', lat: 51.0198, lng: -3.1432, units: 310, status: 'Active' },
		{ name: 'Persimmon at Chippenham', builder: 'Persimmon Homes', lat: 51.4576, lng: -2.1187, units: 420, status: 'Active' },
		// Scotland
		{ name: 'Blindwells', builder: 'Miller Homes', lat: 55.9432, lng: -2.9876, units: 1600, status: 'Active' },
		{ name: 'Shawfair', builder: 'Miller Homes', lat: 55.8987, lng: -3.0765, units: 4000, status: 'Active' },
		{ name: 'CALA at Gilmerton', builder: 'CALA Homes', lat: 55.9012, lng: -3.1543, units: 350, status: 'Active' },
		{ name: 'Barratt at Winchburgh', builder: 'Barratt Developments', lat: 55.9543, lng: -3.5012, units: 3450, status: 'Active' },
		{ name: 'Keepmoat at Dundee', builder: 'Keepmoat', lat: 56.4621, lng: -2.9876, units: 240, status: 'Active' }
	];

	function scoreColour(score: number): string {
		if (score >= 95) return '#3D7A52';
		if (score >= 90) return '#E8960C';
		return '#E03A2F';
	}

	function scoreClass(score: number): string {
		if (score >= 95) return 'score-high';
		if (score >= 90) return 'score-mid';
		return 'score-low';
	}

	function haversine(lat1: number, lng1: number, lat2: number, lng2: number): number {
		const R = 3958.8;
		const dLat = ((lat2 - lat1) * Math.PI) / 180;
		const dLng = ((lng2 - lng1) * Math.PI) / 180;
		const a =
			Math.sin(dLat / 2) ** 2 +
			Math.cos((lat1 * Math.PI) / 180) *
				Math.cos((lat2 * Math.PI) / 180) *
				Math.sin(dLng / 2) ** 2;
		return R * 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
	}

	let mapContainer: HTMLDivElement;
	let L: any;
	let leafletMap: any;
	let markers: any[] = [];
	let locationMarker: any = null;

	let searchInput = $state('');
	let searchHint = $state(
		'Enter a UK postcode to find new build developments and their builder ratings nearby.'
	);
	let sidebarTitle = $state('Developments near you');
	let sidebarSub = $state('Search a postcode to get started');
	let nearbyDevs: (Development & { dist: number })[] = $state([]);
	let searching = $state(false);
	let inputError = $state(false);
	let activeCardIdx = $state(-1);
	let hasSearched = $state(false);

	function makeDots(score: number): string {
		const filled = Math.round((score - 85) / 3);
		let dots = '';
		for (let i = 0; i < 5; i++) {
			const col = i < filled ? scoreColour(score) : '#D8E8DE';
			dots += `<span style="display:inline-block;width:8px;height:8px;border-radius:50%;background:${col};margin-right:3px;"></span>`;
		}
		return dots;
	}

	function createMarkerIcon(score: number) {
		const col = scoreColour(score);
		const svg = `<svg xmlns="http://www.w3.org/2000/svg" width="32" height="40" viewBox="0 0 32 40">
      <path d="M16 0C7.163 0 0 7.163 0 16c0 10 16 24 16 24S32 26 32 16C32 7.163 24.837 0 16 0z" fill="${col}"/>
      <circle cx="16" cy="15" r="9" fill="white" opacity="0.95"/>
      <text x="16" y="19" text-anchor="middle" font-size="9" font-weight="800" font-family="Nunito,sans-serif" fill="${col}">${score.toFixed(0)}%</text>
    </svg>`;
		return L.divIcon({ html: svg, className: '', iconSize: [32, 40], iconAnchor: [16, 40], popupAnchor: [0, -42] });
	}

	function addMarkers(devs: Development[]) {
		markers.forEach((m) => leafletMap.removeLayer(m));
		markers = [];
		devs.forEach((dev, i) => {
			const info = BUILDER_SCORES[dev.builder] ?? { score: 91.0, trend: 'stable', hbfStar: 4 };
			const score = info.score;
			const col = scoreColour(score);
			const barWidth = Math.round(((score - 85) / 15) * 100);
			const marker = L.marker([dev.lat, dev.lng], { icon: createMarkerIcon(score) });
			const popup = `
        <div style="padding:1rem;">
          <div style="font-size:14px;font-weight:800;color:#1E2D24;margin-bottom:2px;">${dev.builder}</div>
          <div style="font-size:12px;color:#6B7A6F;font-weight:600;margin-bottom:0.6rem;">${dev.name} · ${dev.units.toLocaleString()} homes</div>
          <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:0.6rem;">
            <div style="font-family:'Lora',serif;font-size:22px;font-weight:700;color:${col};">${score.toFixed(1)}%</div>
            <div style="font-size:11px;color:#6B7A6F;font-weight:600;text-align:right;">Would recommend<br>their builder</div>
          </div>
          <div style="height:6px;background:#D8E8DE;border-radius:3px;margin-bottom:0.6rem;overflow:hidden;">
            <div style="width:${barWidth}%;height:100%;background:${col};border-radius:3px;"></div>
          </div>
          <div style="font-size:11px;color:#6B7A6F;font-weight:600;">HBF ${info.hbfStar}-star · Trend: ${info.trend}</div>
        </div>
        <div style="background:#EBF4EE;padding:0.6rem 1rem;font-size:11px;font-weight:700;color:#2A5A3A;">Data: WhoBuilt · whobuilt.org</div>
      `;
			marker.bindPopup(popup, { maxWidth: 260, closeButton: true });
			marker.on('click', () => { activeCardIdx = i; });
			marker.addTo(leafletMap);
			markers.push(marker);
		});
	}

	async function searchPostcode() {
		const raw = searchInput.trim().toUpperCase().replace(/\s+/g, '');
		if (!raw) { inputError = true; return; }
		inputError = false;
		searching = true;
		searchHint = 'Looking up postcode…';

		try {
			const res = await fetch(`https://api.postcodes.io/postcodes/${raw}`);
			const data = await res.json();

			if (data.status !== 200) {
				searchHint = 'Postcode not found — please check and try again.';
				inputError = true;
				searching = false;
				return;
			}

			const { latitude: lat, longitude: lng, admin_district, region } = data.result;
			const nearby = DEVELOPMENTS
				.map((d) => ({ ...d, dist: haversine(lat, lng, d.lat, d.lng) }))
				.filter((d) => d.dist <= 25)
				.sort((a, b) => a.dist - b.dist);

			leafletMap.setView([lat, lng], nearby.length ? 11 : 9, { animate: true });

			if (locationMarker) leafletMap.removeLayer(locationMarker);
			locationMarker = L.circleMarker([lat, lng], {
				radius: 8, color: '#3D7A52', fillColor: '#3D7A52', fillOpacity: 0.9, weight: 2
			}).addTo(leafletMap)
				.bindPopup(`<b style="font-family:Nunito">📍 ${admin_district || raw}</b>`)
				.openPopup();

			addMarkers(nearby);
			nearbyDevs = nearby;
			hasSearched = true;
			activeCardIdx = -1;

			sidebarTitle = `Near ${admin_district || raw}`;
			sidebarSub = `${nearby.length} development${nearby.length !== 1 ? 's' : ''} found within 25 miles`;
			searchHint = `Found ${nearby.length} development${nearby.length !== 1 ? 's' : ''} near ${admin_district || raw}, ${region || ''}. Click a pin or card for details.`;
		} catch {
			searchHint = 'Something went wrong — please try again.';
		}

		searching = false;
	}

	function cardClick(idx: number) {
		activeCardIdx = idx;
		const marker = markers[idx];
		if (marker) {
			leafletMap.setView(marker.getLatLng(), 14, { animate: true });
			marker.openPopup();
		}
	}

	onMount(async () => {
		L = (await import('leaflet')).default;
		leafletMap = L.map(mapContainer, { center: [52.5, -1.5], zoom: 6, zoomControl: true });
		L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
			attribution: '© <a href="https://openstreetmap.org/copyright">OpenStreetMap</a> contributors',
			maxZoom: 19
		}).addTo(leafletMap);
		addMarkers(DEVELOPMENTS);
	});
</script>

<svelte:head>
	<title>Builder Map — WhoBuilt</title>
	<meta name="description" content="Search by postcode to see how housebuilders rate in your area." />
</svelte:head>

<div class="map-page">
	<div class="proto-banner">
		Prototype — using representative development data. Full live data launching with WhoBuilt ·
		<a href="/" style="color:var(--color-red-dark);">join the waitlist</a>
	</div>

	<div class="search-bar">
		<div class="search-inner">
			<div class="search-label">Search by postcode</div>
			<div class="search-row">
				<input
					type="text"
					bind:value={searchInput}
					class:error={inputError}
					placeholder="e.g. SW1A 1AA or M1 1AE"
					maxlength={8}
					onkeydown={(e) => e.key === 'Enter' && searchPostcode()}
				/>
				<button onclick={searchPostcode} disabled={searching}>
					{searching ? 'Searching…' : 'Search'}
				</button>
			</div>
			<div class="search-hint">{searchHint}</div>
		</div>
	</div>

	<div class="map-main">
		<div class="sidebar">
			<div class="sidebar-header">
				<div class="sidebar-title">{sidebarTitle}</div>
				<div class="sidebar-sub">{sidebarSub}</div>
			</div>
			<div class="legend">
				<div class="legend-item">
					<div class="legend-dot" style="background:#3D7A52"></div>
					95%+ excellent
				</div>
				<div class="legend-item">
					<div class="legend-dot" style="background:#E8960C"></div>
					90–95% good
				</div>
				<div class="legend-item">
					<div class="legend-dot" style="background:#E03A2F"></div>
					&lt;90% poor
				</div>
			</div>
			<div class="cards-list">
				{#if !hasSearched}
					<div class="empty-state">
						<div class="empty-icon">🏠</div>
						<div class="empty-title">Enter a postcode above</div>
						<div class="empty-sub">
							We'll show you every major new build development within 25 miles, ranked by builder
							satisfaction score.
						</div>
					</div>
				{:else if nearbyDevs.length === 0}
					<div class="empty-state">
						<div class="empty-icon">🔍</div>
						<div class="empty-title">No developments found</div>
						<div class="empty-sub">
							Try a different postcode or a nearby town. We're adding more developments before
							launch.
						</div>
					</div>
				{:else}
					{#each nearbyDevs as dev, i}
						{@const info = BUILDER_SCORES[dev.builder] ?? { score: 91.0, trend: 'stable', hbfStar: 4 }}
						{@const score = info.score}
						<button class="builder-card" class:active={activeCardIdx === i} onclick={() => cardClick(i)}>
							<div class="card-top">
								<div>
									<div class="card-builder">{dev.builder.replace(' Developments', '').replace(' Group', '')}</div>
									<div class="card-dev">{dev.name}</div>
								</div>
								<div class="score-badge {scoreClass(score)}">{score.toFixed(1)}%</div>
							</div>
							<div class="card-meta">
								{dev.units.toLocaleString()} homes · HBF {info.hbfStar}★ · {info.trend}
							</div>
							<div class="rating-row">{@html makeDots(score)}</div>
							{#if dev.dist !== undefined}
								<div class="card-dist">{dev.dist.toFixed(1)} miles away</div>
							{/if}
						</button>
					{/each}
				{/if}
			</div>
		</div>

		<div bind:this={mapContainer} id="map"></div>
	</div>
</div>

<style>
	.map-page {
		display: flex;
		flex-direction: column;
		height: calc(100vh - var(--nav-height));
		overflow: hidden;
		font-family: var(--font-sans);
	}

	.proto-banner {
		background: var(--color-red-light);
		border-bottom: 1px solid #f5bfbb;
		padding: 6px 1.5rem;
		text-align: center;
		font-size: 11px;
		font-weight: 700;
		color: var(--color-red-dark);
		flex-shrink: 0;
	}

	.search-bar {
		background: var(--color-bg-card);
		border-bottom: 1.5px solid var(--color-border);
		padding: 0.875rem 1.5rem;
		flex-shrink: 0;
	}

	.search-inner {
		max-width: 700px;
		margin: 0 auto;
	}

	.search-label {
		font-size: 12px;
		font-weight: 800;
		color: var(--color-muted);
		text-transform: uppercase;
		letter-spacing: 0.06em;
		margin-bottom: 0.5rem;
	}

	.search-row {
		display: flex;
		gap: 8px;
	}

	.search-row input {
		flex: 1;
		padding: 10px 14px;
		font-size: 15px;
		font-family: var(--font-sans);
		font-weight: 700;
		border: 2px solid var(--color-border);
		border-radius: var(--radius-sm);
		background: var(--color-bg);
		color: var(--color-ink);
		outline: none;
		transition: border-color 0.15s;
		text-transform: uppercase;
		letter-spacing: 0.05em;
	}

	.search-row input::placeholder {
		text-transform: none;
		letter-spacing: 0;
		font-weight: 600;
		color: var(--color-muted);
	}

	.search-row input:focus {
		border-color: var(--color-sage);
	}

	.search-row input.error {
		border-color: var(--color-red);
	}

	.search-row button {
		padding: 10px 20px;
		background: var(--color-sage);
		color: #fff;
		font-size: 14px;
		font-weight: 800;
		font-family: var(--font-sans);
		border: none;
		border-radius: var(--radius-sm);
		cursor: pointer;
		transition: background 0.15s;
		white-space: nowrap;
	}

	.search-row button:hover {
		background: var(--color-sage-dark);
	}

	.search-row button:disabled {
		background: var(--color-muted);
		cursor: not-allowed;
	}

	.search-hint {
		font-size: 11px;
		color: var(--color-muted);
		font-weight: 600;
		margin-top: 5px;
	}

	.map-main {
		display: flex;
		flex: 1;
		overflow: hidden;
	}

	.sidebar {
		width: 340px;
		flex-shrink: 0;
		background: var(--color-bg-card);
		border-right: 1.5px solid var(--color-border);
		overflow-y: auto;
		display: flex;
		flex-direction: column;
	}

	.sidebar-header {
		padding: 1rem 1.25rem 0.75rem;
		border-bottom: 1px solid var(--color-border);
	}

	.sidebar-title {
		font-family: var(--font-serif);
		font-size: 16px;
		font-weight: 700;
		color: var(--color-ink);
	}

	.sidebar-sub {
		font-size: 11px;
		color: var(--color-muted);
		font-weight: 600;
		margin-top: 2px;
	}

	.legend {
		padding: 0.75rem 1.25rem;
		border-bottom: 1px solid var(--color-border);
		display: flex;
		gap: 12px;
		align-items: center;
		flex-wrap: wrap;
	}

	.legend-item {
		display: flex;
		align-items: center;
		gap: 5px;
		font-size: 11px;
		font-weight: 700;
		color: var(--color-muted);
	}

	.legend-dot {
		width: 10px;
		height: 10px;
		border-radius: 50%;
		flex-shrink: 0;
	}

	.cards-list {
		flex: 1;
		padding: 0.75rem;
		display: flex;
		flex-direction: column;
		gap: 8px;
	}

	.empty-state {
		padding: 2rem 1.25rem;
		text-align: center;
	}

	.empty-icon {
		font-size: 32px;
		margin-bottom: 0.75rem;
	}

	.empty-title {
		font-size: 14px;
		font-weight: 800;
		color: var(--color-ink);
		margin-bottom: 0.4rem;
	}

	.empty-sub {
		font-size: 12px;
		color: var(--color-muted);
		font-weight: 600;
		line-height: 1.5;
	}

	.builder-card {
		background: var(--color-bg);
		border-radius: var(--radius-sm);
		padding: 1rem;
		border: 1.5px solid var(--color-border);
		cursor: pointer;
		transition:
			border-color 0.15s,
			transform 0.15s;
		text-align: left;
		width: 100%;
		font-family: var(--font-sans);
	}

	.builder-card:hover {
		border-color: var(--color-sage);
		transform: translateY(-1px);
	}

	.builder-card.active {
		border-color: var(--color-sage);
		background: var(--color-sage-light);
	}

	.card-top {
		display: flex;
		align-items: flex-start;
		justify-content: space-between;
		margin-bottom: 0.5rem;
	}

	.card-builder {
		font-size: 13px;
		font-weight: 800;
		color: var(--color-ink);
	}

	.card-dev {
		font-size: 11px;
		color: var(--color-muted);
		font-weight: 600;
		margin-top: 1px;
	}

	.card-meta {
		font-size: 11px;
		color: var(--color-muted);
		font-weight: 600;
		margin-bottom: 0.5rem;
	}

	.rating-row {
		display: flex;
		gap: 3px;
		align-items: center;
	}

	.card-dist {
		font-size: 11px;
		color: var(--color-sage);
		font-weight: 700;
		margin-top: 0.4rem;
	}

	#map {
		flex: 1;
		z-index: 1;
	}

	@media (max-width: 640px) {
		.map-main {
			flex-direction: column-reverse;
		}
		.sidebar {
			width: 100%;
			height: 280px;
			border-right: none;
			border-top: 1.5px solid var(--color-border);
		}
		#map {
			flex: 1;
			min-height: 300px;
		}
	}
</style>
