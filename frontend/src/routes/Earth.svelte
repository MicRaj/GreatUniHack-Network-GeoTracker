<script>
  import { onMount } from "svelte";
  import { browser } from "$app/environment";
  let earth;
  let N = 20;
  let arcsData = Array.from({ length: N }, () => ({
    startLat: 53.484824,
    startLng: -2.240126,
    endLat: 38.897957,
    endLng: -77.03656,
    color: [
      ["red", "white", "blue", "green"][Math.round(Math.random() * 3)],
      ["red", "white", "blue", "green"][Math.round(Math.random() * 3)],
    ],
  }));

  onMount(async () => {
    if (browser) {
      const Globe = (await import("globe.gl")).default;
      earth = Globe()
        .globeImageUrl("/2k_earth_daymap.jpg")
        .width(2100)
        .showGraticules(true)
        .showAtmosphere(false)
        .arcsData(arcsData)
        .arcColor("color")
        .arcDashLength(0.9)
        .arcDashGap(1.0)
        .arcDashAnimateTime(() => Math.random() * 4000 + 500)
        .backgroundImageUrl("/2k_stars.jpg")(document.getElementById("earth"));
    }
  });

  function addNewArc() {
    arcsData = [
      ...arcsData,
      {
        startLat: 55.7558,
        startLng: 37.6173,
        endLat: 47.751076,
        endLng: -120.740135,
        color: "red",
      },
    ];
    earth.arcsData(arcsData);
    console.log(arcsData); // To verify that the new line is added
  }
</script>

<div class="position">
  <div class="border">
    <div class="data">
      <div class="title">
        <h1>dadffdadas</h1>
      </div>
      <div class="graphs">
        <h1>graph1</h1>
        <h1>graph2</h1>
        <h1>graph3</h1>
        <h1>graph4</h1>
      </div>
    </div>
  </div>

  <div id="earth"></div>
</div>

<style>
  div.position {
    display: flex;
    overflow: hidden;
  }
  div#earth {
    z-index: 1;
  }
  div.data {
    display: flex;
    flex-wrap: wrap;
    z-index: 2;
  }
  div.data h1 {
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
    
  }
  div.border {
    font-family: 'RobotoMono-Regular', monospace;
    position: absolute;
    width: 568px;
    height: 500px;
    top: 200px;
    left: 83px;
    z-index: 3;
    background-color: #0C0C0C;
    color: white;
    opacity: 65%;
    overflow-y: hidden;
    scrollbar-gutter: stable both-edges;
  }
  div.border:hover{
    overflow-y: scroll;
    scrollbar-width: thin;
    
  }
  div.title {
    width: 100%;
    height: 100px;
    margin: 5px;
    padding: 10px;
  }
  div.graphs {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
    
  }
  div.graphs h1 {
    padding: 40px;
  }
</style>
