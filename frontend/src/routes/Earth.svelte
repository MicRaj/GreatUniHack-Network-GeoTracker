<script>
  import { onMount } from "svelte";
  import { browser } from "$app/environment";
  export let earth;
  let Globe;

  let selectedTitle = "Select a node!";

  onMount(async () => {
    if (browser) {
      Globe = (await import("globe.gl")).default;
    }
  });

  export function updateArcs(arcsData) {
    earth = Globe()
    .onArcClick((arc) => arcclick(arc))
        .globeImageUrl("/nasa_hq.jpg")
        .width(2100)
        .showGraticules(true)
        .showAtmosphere(true)
        .arcStroke(1.5)
        .arcsData(arcsData)
        .arcColor("color")
        .arcDashLength(0.9)
        .arcStroke(1.5)
        // .arcDashGap(1.0)
        // .arcDashAnimateTime(() => Math.random() * 4000 + 500)
        .backgroundImageUrl("/2k_stars.jpg")(document.getElementById("earth"))
        .arcsData(arcsData);
  }

  function arcclick(arc){//templpate function for on click stuff
    console.log(arc)
    console.log(arc.color);
    if (arc._orig.place != ""){
      selectedTitle = arc._orig.place
    } else {
      selectedTitle = arc._orig.registered_country;
    }
  }
</script>

<div class="position">
  <div class="border">
    <div class="data">
      <div class="title">
        <h1 id="title">{selectedTitle}</h1>
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
    background-color: rgba(12, 12, 12, 0.8);
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
