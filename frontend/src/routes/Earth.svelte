<script>
  import { onMount } from "svelte";
  import { browser } from "$app/environment";
  let earth;
  let N = 20;
  export let arcsData;

  onMount(async () => {
    if (browser) {
      const Globe = (await import("globe.gl")).default;
      earth = Globe()
        .globeImageUrl("/2k_earth_daymap.jpg")
        .width(2200)
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
    // earth.arcsData(arcsData);
    console.log(arcsData); // To verify that the new line is added
  }
  function updateArcs() {
    if (earth) {
      earth.arcsData(arcsData);
    }
  }
  $: updateArcs();
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
        <button id="line-test" on:click={addNewArc}>click me</button>
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
    position: absolute;
    width: 432px;
    top: 240px;
    left: 108px;
    z-index: 3;
    background-color: white;
  }
  div.title {
    width: 100%;
    height: 50px;
    margin: 5px;
    padding: 10px;
    border: 1px solid black;
  }
  div.graphs {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
  }
  div.graphs h1 {
    border: 1px solid black;
    padding: 40px;
  }
</style>
