<script>
  import Navbar from "../Navbar.svelte";
  import Timeline from "../Timeline.svelte";

  let marker1Position = 0;
  let marker2Position = 1;

</script>
<Navbar />
<Timeline bind:normPos1={marker1Position} bind:normPos2={marker2Position} timelineWidth=1000/>
<div>
  <p>Marker 1 Position: {marker1Position}</p>
  <p>Marker 2 Position: {marker2Position}</p>
</div>