<script>
    import { onMount } from 'svelte';
    import { browser } from '$app/environment';

onMount(async() => {
    if (browser) {

        // Gen random data
        const N = 20;
        const arcsData = [...Array(N).keys()].map(() => ({
        startLat: (Math.random() - 0.5) * 180,
        startLng: (Math.random() - 0.5) * 360,
        endLat: (Math.random() - 0.5) * 180,
        endLng: (Math.random() - 0.5) * 360,
        color: [['red', 'white', 'blue', 'green'][Math.round(Math.random() * 3)], ['red', 'white', 'blue', 'green'][Math.round(Math.random() * 3)]]
        }));

        const Globe = (await import('globe.gl')).default;
        const earth = Globe()
            .globeImageUrl('/2k_earth_xray_map.png')
            .width(2200)
            .showGraticules(true)
            .showAtmosphere(false)
            .arcsData(arcsData)
            .arcColor('color')
            .arcDashLength(0.9)
            .arcDashGap(4.0)
            .arcDashAnimateTime(() => Math.random() * 4000 + 500)
            .backgroundImageUrl('/2k_stars.jpg')
        (document.getElementById('earth'))
    }
});


</script>

<style>

    div.position {
       display: flex;   
        overflow: hidden;
        
    }
    div#earth {
        z-index: 1;
    }
    div.data{
        z-index: 2;
    }
    div.border{
        position: absolute;
        width: 432px;
        top: 240px;
        left: 108px;
        border: 1px solid black;
        z-index: 3;
        background-color: white;
    }


</style>
<div class="position">
    <div class="border">
    <div class="data">
        <h1>dadffdadas</h1>
    </div>        
    </div>

<div id="earth" ></div>
</div>