<script>
    import { onMount } from 'svelte';
    import { browser } from '$app/environment';

onMount(async() => {
    if (browser) {
        const Globe = (await import('globe.gl')).default;
        const earth = Globe()
            .globeImageUrl('/2k_earth_xray_map.png')
            .width(300)
            .height(300)
            .showGraticules(true)
            .showAtmosphere(false)
        (document.getElementById('earth'))
    }
});
</script>

<style>
    div.border {
        display: flex;
        justify-content: center;
        border: 1px solid black;
        width: 30vh;
    }
    div.position {
        display: flex;
        justify-content: center;
        margin-top: 10vh;
    }

</style>
<div class="position">
<div class="border">
<div id="earth"></div>
</div>
</div>