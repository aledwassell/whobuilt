<script lang="ts">
	import './layout.css';
	import type { Snippet } from 'svelte';
	import { page } from '$app/state';

	let { children }: { children: Snippet } = $props();

	const navLinks = [
		// { href: '/map', label: 'Map' },
		{ href: '/data', label: 'Data' },
		{ href: '/builders', label: 'Builders' }
		// { href: '/methodology', label: 'Methodology' },
		// { href: '/about', label: 'About' }
	];
</script>

<svelte:head>
	<!-- Google Analytics -->
	<script async src="https://www.googletagmanager.com/gtag/js?id=G-G6QF3KLYXJ"></script>
	<script>
		window.dataLayer = window.dataLayer || [];
		function gtag() {
			dataLayer.push(arguments);
		}
		gtag('js', new Date());
		gtag('config', 'G-G6QF3KLYXJ');
	</script>

	<!-- Fonts -->
	<link rel="preconnect" href="https://fonts.googleapis.com" />
	<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="true" />
	<link
		href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&family=Lora:ital,wght@0,600;0,700;1,600;1,700&display=swap"
		rel="stylesheet"
	/>
</svelte:head>

<nav class="site-nav">
	<div class="site-nav-inner">
		<a href="/" class="flex flex-shrink-0 items-center gap-2 no-underline">
			<div class="flex h-8 w-8 items-center justify-center rounded-[9px] bg-[var(--color-sage)]">
				<svg width="18" height="18" viewBox="0 0 20 20" fill="none">
					<path
						d="M4 15L10 5L16 15"
						stroke="#fff"
						stroke-width="2.5"
						stroke-linecap="round"
						stroke-linejoin="round"
					/>
					<circle cx="10" cy="16.5" r="1.5" fill="#fff" />
				</svg>
			</div>
			<span class="text-[17px] font-black text-[var(--color-ink)]">WhoBuilt</span>
		</a>

		<div class="site-nav-links">
			{#each navLinks as link}
				<a
					href={link.href}
					class="site-nav-link"
					class:active={page.url.pathname.startsWith(link.href)}
				>
					{link.label}
				</a>
			{/each}
		</div>

		<a href="/#waitlist" class="site-nav-cta">Join waitlist</a>
	</div>
</nav>

{@render children()}
