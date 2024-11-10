<script>
  import Navbar from "../Navbar.svelte";
  import Timeline from "../Timeline.svelte";
  import Earth from "../Earth.svelte";

  let marker1Position = 0;
  let marker2Position = 1;
  let loading = false;
  let error;
  let data;

  // Function to fetch data from an API
  async function fetchData() {
    try {
      // Set loading to true while fetching data
      loading = true;
      // Replace with your API endpoint
      const response = await fetch("http://127.0.0.1:8000/items/"); // TODO ROUTE

      if (!response.ok) {
        throw new Error(`Error: ${response.status}`);
      }

      // Parse the JSON response
      data = await response.json();
    } catch (err) {
      error = err.message;
      console.log(error);
    } finally {
      loading = false;
    }
  }
</script>

<Navbar />
<Timeline
  bind:normPos1={marker1Position}
  bind:normPos2={marker2Position}
  timelineWidth="1000"
  sendGetRequest={fetchData}
/>
<div>
  <p>Marker 1 Position: {marker1Position}</p>
  <p>Marker 2 Position: {marker2Position}</p>
</div>
<Earth />
