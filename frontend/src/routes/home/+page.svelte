<script>
  import Timestamp from "../Timestamp.svelte";
  import Timeline from "../Timeline.svelte";
  import Earth from "../Earth.svelte";

  let marker1Position = 0;
  let marker2Position = 1;
  let loading = false;
  let error;
  let data;
  let earth;

  // Get current date and time
  let currentDateTime = new Date();
  // Convert to epoch time in seconds
  let present = Math.floor(currentDateTime.getTime() / 1000);
  let past = present - 86400; // 24 hours ago

  // Set the epoch time for the timestamps
  $: epochTime1 = Math.floor(past + (present - past) * marker1Position);
  $: epochTime2 = Math.floor(past + (present - past) * marker2Position);

  // Function to fetch data from an API
  async function fetchData() {
    try {
      // Set loading to true while fetching data
      loading = true;
      // Replace with your API endpoint
      const response = await fetch(
        `http://127.0.0.1:8000/data?starttime=${epochTime1}&endtime=${epochTime2}`
      ); // TODO ROUTE

      if (!response.ok) {
        throw new Error(`Error: ${response.status}`);
      }

      // Parse the JSON response
      data = await response.json();

      console.log("HERE")
      earth.updateArcs([{
        startLat: 0,
        startLng: 0,
        endLat: 89,
        endLng: 32,
        color: "red"
      }]);

    } catch (err) {
      error = err.message;
      console.log(error);
    } finally {
      loading = false;
    }
  }

  // Get user coordinates on page load.
  let latitude = null;
  let longitude = null;
  let errorMessage = null;

  // Function to get the user's coordinates
  function getCoordinates() {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(
        (position) => {
          // Success: Get the latitude and longitude from the position object
          latitude = position.coords.latitude;
          longitude = position.coords.longitude;
          console.log(latitude, longitude);
          errorMessage = null; // Clear any previous errors
        },
        (error) => {
          // Error: Handle geolocation errors
          switch (error.code) {
            case error.PERMISSION_DENIED:
              errorMessage = "User denied the request for Geolocation.";
              break;
            case error.POSITION_UNAVAILABLE:
              errorMessage = "Location information is unavailable.";
              break;
            case error.TIMEOUT:
              errorMessage = "The request to get user location timed out.";
              break;
            case error.UNKNOWN_ERROR:
              errorMessage = "An unknown error occurred.";
              break;
          }
        }
      );
    } else {
      errorMessage = "Geolocation is not supported by this browser.";
    }
  }

  // Call the function to get coordinates when the component is mounted
  import { onMount } from "svelte";
  onMount(getCoordinates);
</script>


<div class="timestamp-container">
  <div class="left">
    <Timestamp bind:epochTime={epochTime1} />
  </div>
  <div class="right">
    <Timestamp bind:epochTime={epochTime2} />
  </div>
</div>
<Timeline
  bind:normPos1={marker1Position}
  bind:normPos2={marker2Position}
  timelineWidth="1550"
  sendGetRequest={fetchData}
/>
<Earth bind:this={earth}/>

<style>
  .timestamp-container {
    position: absolute;
    display: flex;
    justify-content: space-between;
    z-index: 4;
    align-items: center;
    padding-top: 20px;
    pointer-events: none;
  }
  .left{

    padding-right: 10%;
    padding-left: 10%;
    pointer-events: none;
  }
  .right{
    padding-right: 10%;
    padding-left: 149%;
    pointer-events: none;
  }

  .timestamp-container > * {
    flex: 0 1 auto;
    font-size: 1.2em;
  }
</style>
