<script>
  import { onMount } from "svelte";
  import { browser } from "$app/environment";
  import { passive } from "svelte/legacy";
  export let earth;
  export let epochTime1;
  export let epochTime2;

  let Globe;

  onMount(async () => {
    if (browser) {
      Globe = (await import("globe.gl")).default;
    }
    updateArcs([
      {
        startLat: 0,
        startLng: 0,
        endLat: 51.2,
        endLng: 0,
        color: "red",
      },
    ]);
  });

  export function updateArcs(arcsData) {
    earth = Globe()
      .globeImageUrl("/2k_earth_daymap.jpg")
      .width(2100)
      .showGraticules(true)
      .showAtmosphere(true)
      .arcColor("color")
      .arcDashLength(0.9)
      .arcDashGap(1.0)
      .arcDashAnimateTime(() => Math.random() * 4000 + 500)
      .backgroundImageUrl("/2k_stars.jpg")(document.getElementById("earth"))
      .arcsData(arcsData);
  }

  let UPD_count = 0;
  let TCP_count = 0;
  let TCP_size = 0;
  let UDP_size = 0;

  async function getStatistics(t1, t2) {
    try {
      const response = await fetch(
        `http://127.0.0.1:8000/getStats?starttimestamp=${t1}&endtimestamp=${t2}`
      );

      if (!response.ok) {
        throw new Error(`Error: ${response.status}`);
      }

      const data = await response.json();

      // Loop through the data and create div elements for each protocol

      document.getElementById("UDP_stats").setAttribute("display", "none");
      document.getElementById("TCP_stats").setAttribute("display", "none");

      data.forEach((protocol) => {
        if (protocol.protocol === "UDP") {
          document.getElementById("UDP_stats").setAttribute("display", "block");
          UDP_size = protocol.size;
          UPD_count = protocol.count;
        } else if (protocol.protocol === "TCP") {
          document.getElementById("TCP_stats").setAttribute("display", "block");
          TCP_size = protocol.size;
          TCP_count = protocol.count;
        }
      });
    } catch (err) {
      console.log(err);
    }
  }

  $: stats = getStatistics(epochTime1, epochTime2);
</script>

<div class="position">
  <div class="border">
    <div class="data">
      <h1>Statistics</h1>
      <div id="UDP_stats" display="none" class="stats_stuff">
        <h2 class="title">UDP</h2>
        <div class="graphs">
          <p class="count_num">{UPD_count} packets sent</p>
          <p class="size_num">
            {Math.round((UDP_size / 1048576) * 100) / 100} MB total size
          </p>
        </div>
      </div>
      <div id="TCP_stats" display="none" class="stats_stuff">
        <h2 class="title">TCP</h2>
        <div class="graphs">
          <p class="count_num">{TCP_count} packets sent</p>
          <p class="size_num">
            {Math.round((TCP_size / 1048576) * 100) / 100} MB total size
          </p>
        </div>
      </div>
    </div>
  </div>
  <div id="earth"></div>
</div>

<style>
  .stats_stuff {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    align-items: center;
    /* justify-content: center; */
    z-index: 2;
    margin-bottom: 30px;
  }

  .title {
    margin-right: 20px;
    font-size: 30px;
  }

  .count_num {
    margin-right: 20px;
    font-size: 20px;
    font-weight: bold;
    color: #ffffff;
  }

  .size_num {
    margin-right: 20px;
    font-size: 20px;
    font-weight: bold;
    color: #ffffff;
  }

  .graphs {
    display: flex;
    flex-direction: column;
    margin-left: 40px;
  }

  div.position {
    display: flex;
    overflow: hidden;
  }

  div#earth {
    z-index: 1;
  }
  div.data {
    display: flex;
    flex-direction: column;
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
    font-family: "RobotoMono-Regular", monospace;
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
  /* div.border:hover {
    overflow-y: scroll;
    scrollbar-width: thin;
  } */
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
