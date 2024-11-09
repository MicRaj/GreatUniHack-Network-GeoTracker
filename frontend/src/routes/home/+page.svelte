<script>
  import Navbar from "../Navbar.svelte";
  import Timeline from "../Timeline.svelte";

  let marker1Position = 0;
  let marker2Position = 300;
</script>
<Navbar />
<Timeline bind:marker1Position bind:marker2Position />
<div>
  <p>Marker 1 Position: {marker1Position}</p>
  <p>Marker 2 Position: {marker2Position}</p>
</div>