<script>
    import { onMount } from 'svelte';
    import { browser } from '$app/environment';

onMount(async() => {
    if (browser) {

        // Gen random data
        const N = 20;
        const arcsData = [...Array(N).keys()].map(() => ({
        startLat: 53.484824,
        startLng: -2.240126,
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
        display: flex;
        flex-wrap: wrap;
        z-index: 2;
    }
    div.data h1{
        display: flex;
        justify-content: center;
        align-items: center;
        text-align: center;
    }
    div.border{
        position: absolute;
        width: 432px;
        top: 240px;
        left: 108px;
        z-index: 3;
        background-color: white;
    }
    div.title{
        width: 100%;
        height: 50px;
        margin: 5px;
        padding: 10px;
        border: 1px solid black;

    }
    div.graphs{
        display: flex;
        flex-wrap: wrap;
        justify-content: space-around;
    }
    div.graphs h1{  
        border: 1px solid black;
        padding: 40px;
    }


</style>
<div class="position">
    <div class="border">
    <div class="data">
        <div class="title">
        <h1>dadffdadas</h1>
    </div>
       <div class="graphs"><h1> graph1</h1> <h1> graph2</h1><h1> graph3</h1><h1> graph4</h1>
    </div> 
    </div>        
    </div>

<div id="earth" ></div>
</div>