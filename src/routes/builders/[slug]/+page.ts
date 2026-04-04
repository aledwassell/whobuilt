import { builders } from '$lib/data/builders';
import { error } from '@sveltejs/kit';

export const prerender = true;

export function entries() {
	return builders.map((b) => ({ slug: b.slug }));
}

export function load({ params }) {
	const builder = builders.find((b) => b.slug === params.slug);
	if (!builder) error(404, 'Builder not found');
	return { builder };
}
