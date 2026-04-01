<script lang="ts">
  import './layout.css';
  import type { Snippet } from 'svelte';

  let { children }: { children: Snippet } = $props();
</script>
 
<svelte:head>
  <!-- Google Analytics -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-G6QF3KLYXJ"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag() { dataLayer.push(arguments); }
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
 
<!-- Each page renders here -->
{@render children()}
 
