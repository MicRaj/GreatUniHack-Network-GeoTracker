<script>
  import { onMount } from "svelte";
  import { browser } from "$app/environment";
  let earth;
  let N = 20;
  let arcsData = Array.from({ length: N }, () => ({
    startLat: [Math.round(Math.random() * 3)] *180,
    startLng: [Math.round(Math.random() * 3)] *360,
    endLat: [Math.round(Math.random() * 3)] *360,
    endLng: [Math.round(Math.random() * 3)] *180,
    color: [
      ["red", "white", "blue", "green"][Math.round(Math.random() * 3)],
      ["red", "white", "blue", "green"][Math.round(Math.random() * 3)],
    ],
  }));

  onMount(async () => {
    if (browser) {
      const Globe = (await import("globe.gl")).default;
      earth = Globe()
      .onArcClick((arc) => arcclick(arc))// ON CLICK TEMPLATE FUNCTION
        .globeImageUrl("/2k_earth_daymap.jpg")
        .width(2100)
        .showGraticules(true)
        .showAtmosphere(false)
        .arcStroke(1.5)
        .arcsData(arcsData)
        .arcColor("color")
        .arcDashLength(0.9)
        .arcDashGap(0.5)
        .arcDashAnimateTime(() => Math.random() * 4000 + 500)
        .backgroundImageUrl("/2k_stars.jpg")(document.getElementById("earth"));
    }
  });
  function arcclick(arc){//templpate function for on click stuff
    let name = document.getElementById("name");
     name.innerText = arc.color;
    console.log(arc.color);

  }
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
        <h1 id="name">dadffdadas</h1>
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
