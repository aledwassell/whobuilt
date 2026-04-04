<script>
	// ── Page metadata ──────────────────────────────────────────────────────
	const FORMSPREE = 'https://formspree.io/f/mzdjypjg';

	// ── Waitlist state ─────────────────────────────────────────────────────
	let email1 = '';
	let email2 = '';
	let error1 = false;
	let error2 = false;
	let sending1 = false;
	let sending2 = false;
	let success1 = false;
	let success2 = false;

	// ── Builder data ───────────────────────────────────────────────────────
	const builders = [
		{ name: 'Barratt Redrow', meta: '~19,000 homes/yr', dots: 4 },
		{ name: 'Taylor Wimpey', meta: '~14,000 homes/yr', dots: 3 },
		{ name: 'Persimmon', meta: '~14,000 homes/yr', dots: 3 },
		{ name: 'Vistry Group', meta: '~17,000 homes/yr', dots: 4 },
		{ name: 'Bellway', meta: '~10,000 homes/yr', dots: 4 },
		{ name: 'Berkeley Group', meta: '~5,000 homes/yr', dots: 5 }
	];

	const features = [
		{
			title: 'Build quality scores',
			body: 'Aggregated ratings across structural defects, finishing, and snagging — verified against NHBC warranty data.',
			icon: `<path d="M4 16L11 6L18 16" stroke="#3D7A52" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><circle cx="11" cy="18" r="1.5" fill="#3D7A52"/>`
		},
		{
			title: 'Verified resident reviews',
			body: 'Post-completion reviews from real homeowners — not purchase-day surveys before problems appear.',
			icon: `<circle cx="8" cy="9" r="3.5" stroke="#3D7A52" stroke-width="2"/><circle cx="15" cy="9" r="3.5" stroke="#3D7A52" stroke-width="2"/><path d="M3 19c0-2.5 2-4 5-4h6c3 0 5 1.5 5 4" stroke="#3D7A52" stroke-width="2" stroke-linecap="round"/>`
		},
		{
			title: 'After-sales tracking',
			body: 'How quickly do builders fix problems? We track responsiveness across the 2-year liability period.',
			icon: `<rect x="4" y="7" width="14" height="12" rx="2" stroke="#3D7A52" stroke-width="2"/><path d="M7 3v4M15 3v4M4 11h14" stroke="#3D7A52" stroke-width="2" stroke-linecap="round"/>`
		},
		{
			title: 'Regional breakdown',
			body: 'A builder strong in the South East can be poor in the Midlands. We surface performance by region.',
			icon: `<path d="M4 18L4 10L8 13L13 6L18 10L18 18Z" stroke="#3D7A52" stroke-width="2" stroke-linejoin="round" fill="none"/>`
		},
		{
			title: 'Value for money',
			body: "What's included as standard vs. what others charge as extras — a true apples-to-apples comparison.",
			icon: `<path d="M11 3L13.5 9L20 9.8L15.5 14L17 20L11 17L5 20L6.5 14L2 9.8L8.5 9Z" stroke="#3D7A52" stroke-width="2" stroke-linejoin="round" fill="none"/>`
		},
		{
			title: 'Sustainability ratings',
			body: 'Real-world EPC performance and energy bills — not developer claims about green credentials.',
			icon: `<path d="M6 18C6 12 8 8 11 6C14 8 16 12 16 18" stroke="#3D7A52" stroke-width="2" stroke-linecap="round"/><path d="M4 18h14" stroke="#3D7A52" stroke-width="2" stroke-linecap="round"/>`
		}
	];

	// ── Signup handler ─────────────────────────────────────────────────────
	async function handleSignup(slot) {
		const isFirst = slot === 1;
		const email = isFirst ? email1 : email2;
		const valid = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.trim());

		if (!valid) {
			if (isFirst) error1 = true;
			else error2 = true;
			return;
		}

		if (isFirst) {
			error1 = false;
			sending1 = true;
		} else {
			error2 = false;
			sending2 = true;
		}

		try {
			const res = await fetch(FORMSPREE, {
				method: 'POST',
				headers: { Accept: 'application/json', 'Content-Type': 'application/json' },
				body: JSON.stringify({ email: email.trim() })
			});

			if (res.ok) {
				if (isFirst) success1 = true;
				else success2 = true;
			} else {
				alert('Something went wrong — please try again.');
			}
		} catch {
			alert('Network error — please try again.');
		} finally {
			if (isFirst) sending1 = false;
			else sending2 = false;
		}
	}
</script>

<!-- ── Page metadata ─────────────────────────────────────────────────── -->
<svelte:head>
	<title>WhoBuilt — Independent New Build Intelligence</title>
	<meta
		name="description"
		content="WhoBuilt is the UK's first independent quality comparison service for new build housebuilders. Join the waitlist."
	/>
	<link rel="icon" type="image/svg+xml" href="/favicon.svg" />
	<link rel="apple-touch-icon" type="image/svg+xml" href="/favicon.svg" />
</svelte:head>

<!-- ── Markup ─────────────────────────────────────────────────────────── -->
<div class="page" id="waitlist">
	<!-- Hero -->
	<section
		class="relative mb-6 overflow-hidden rounded-3xl px-10 py-12"
		style="background: var(--color-sage-light); margin-top: 0.5rem;"
	>
		<!-- Decorative circles -->
		<div
			class="absolute -top-5 -right-5 h-56 w-56 rounded-full opacity-50"
			style="background: var(--color-sage-mid);"
		></div>
		<div
			class="absolute right-16 -bottom-10 h-36 w-36 rounded-full opacity-[0.12]"
			style="background: var(--color-sage);"
		></div>

		<div class="relative z-10">
			<!-- Tag -->
			<div
				class="mb-5 inline-flex items-center gap-1.5 rounded-full px-3 py-1.5 text-[11px] font-extrabold tracking-[0.06em] text-white uppercase"
				style="background: var(--color-sage);"
			>
				<svg width="12" height="12" viewBox="0 0 12 12" fill="none">
					<circle cx="6" cy="6" r="5" stroke="#fff" stroke-width="1.5" />
					<path d="M6 4v3M6 8.5v.5" stroke="#fff" stroke-width="1.5" stroke-linecap="round" />
				</svg>
				Independent · UK new builds
			</div>

			<h1
				class="mb-5 max-w-[580px] font-serif text-[clamp(34px,5vw,56px)] leading-[1.1] font-bold"
				style="color: var(--color-ink);"
			>
				Find out <em style="color: var(--color-red-dark);">who really</em> builds a quality home
			</h1>

			<p class="mb-8 max-w-[540px] text-base leading-relaxed font-semibold" style="color: #3a5040;">
				The honest, independent guide to UK housebuilders — so you can choose with confidence, not
				hope.
			</p>

			<!-- Form -->
			{#if !success1}
				<div class="form-wrap">
					<input
						type="email"
						bind:value={email1}
						class:error={error1}
						placeholder="your@email.com"
						autocomplete="email"
						onkeydown={(e) => e.key === 'Enter' && handleSignup(1)}
					/>
					<button onclick={() => handleSignup(1)} disabled={sending1}>
						{sending1 ? 'Sending…' : 'Join waitlist'}
					</button>
				</div>
				<p
					class="mt-2.5 flex items-center gap-1.5 text-xs font-semibold"
					style="color: var(--color-muted);"
				>
					<svg width="12" height="12" viewBox="0 0 12 12" fill="none">
						<path
							d="M2 6.5l3 3 5-5"
							stroke="#3D7A52"
							stroke-width="1.5"
							stroke-linecap="round"
							stroke-linejoin="round"
						/>
					</svg>
					No spam. Free access to our launch reports for early members.
				</p>
			{:else}
				<p class="pt-2.5 text-[15px] font-extrabold" style="color: var(--color-sage);">
					You're on the list — we'll be in touch before launch.
				</p>
			{/if}
		</div>
	</section>

	<!-- Stats bar -->
	<div class="mb-6 grid gap-3" style="grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));">
		<div class="stat-card">
			<div class="stat-num accent">£31bn</div>
			<div class="stat-label">Annual new build market</div>
		</div>
		<div class="stat-card">
			<div class="stat-num">220k+</div>
			<div class="stat-label">New homes built per year</div>
		</div>
		<div class="stat-card">
			<div class="stat-num accent">1 in 3</div>
			<div class="stat-label">Buyers report major defects</div>
		</div>
		<div class="stat-card">
			<div class="stat-num">Zero</div>
			<div class="stat-label">Independent comparison services — until now</div>
		</div>
	</div>

	<!-- Features -->
	<div class="mb-5 flex items-center gap-2.5 pt-8">
		<div class="section-tag">What we do</div>
	</div>
	<div class="section-title">Everything buyers wish they'd known before signing.</div>

	<div class="mb-6 grid gap-3" style="grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));">
		{#each features as f}
			<div class="feature">
				<div class="feature-icon-wrap">
					<svg width="22" height="22" viewBox="0 0 22 22" fill="none">
						{@html f.icon}
					</svg>
				</div>
				<h3
					class="mb-1.5 text-[15px] font-extrabold"
					style="color: var(--color-ink); font-family: 'Nunito', sans-serif;"
				>
					{f.title}
				</h3>
				<p class="text-sm leading-relaxed font-semibold" style="color: var(--color-muted);">
					{f.body}
				</p>
			</div>
		{/each}
	</div>

	<!-- Builders -->
	<div class="mb-5 flex items-center gap-2.5 pt-8">
		<div class="section-tag">Builders we'll cover</div>
	</div>

	<div
		class="mb-3 grid gap-2.5"
		style="grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));"
	>
		{#each builders as b}
			<div class="builder-card">
				<div class="builder-name">{b.name}</div>
				<div class="builder-meta">{b.meta}</div>
				<div class="flex gap-1">
					{#each Array(5) as _, i}
						<div class="dot" class:filled={i < b.dots}></div>
					{/each}
				</div>
			</div>
		{/each}
	</div>

	<p class="mb-8 text-[11px] font-semibold" style="color: var(--color-muted);">
		Indicative ratings based on publicly available data. Full methodology published at launch.
	</p>

	<!-- Manifesto -->
	<div class="manifesto">
		<blockquote>
			"Buying a new build is one of the largest financial decisions of your life. You deserve better
			than a developer's own five-star survey."
		</blockquote>
		<cite>— The WhoBuilt mission</cite>
	</div>

	<!-- Bottom CTA -->
	<div class="cta-block">
		<div class="section-title">Be first to know.</div>
		<p class="cta-sub">Early members get free access to every report we publish at launch.</p>

		{#if !success2}
			<div class="form-wrap">
				<input
					type="email"
					bind:value={email2}
					class:error={error2}
					placeholder="your@email.com"
					autocomplete="email"
					onkeydown={(e) => e.key === 'Enter' && handleSignup(2)}
				/>
				<button onclick={() => handleSignup(2)} disabled={sending2}>
					{sending2 ? 'Sending…' : 'Notify me'}
				</button>
			</div>
		{:else}
			<p class="pt-2.5 text-[15px] font-extrabold" style="color: var(--color-sage);">
				You're on the list — we'll be in touch before launch.
			</p>
		{/if}
	</div>

	<!-- Footer -->
	<footer class="footer">
		<div class="footer-logo">WhoBuilt</div>
		<div class="footer-copy">
			© 2026 WhoBuilt Ltd · Independent housing intelligence · whobuilt.org
		</div>
	</footer>
</div>
