<script>
  import Timestamp from "../Timestamp.svelte";
  import Timeline from "../Timeline.svelte";
  import Earth from "../Earth.svelte";

  // Get user coordinates on page load.
  let latitude = 0;
  let longitude = 0;
  let errorMessage = null;
  let marker1Position = 0;
  $: arcsData = [];
  let marker2Position = 1;
  let loading = false;
  let error;
  let response;

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
      const webresponse = await fetch(
        `http://127.0.0.1:8000/data?starttime=${epochTime1}&endtime=${epochTime2}`,
      ); // TODO ROUTE

      if (!webresponse.ok) {
        throw new Error(`Error: ${webresponse.status}`);
      }

      // Parse the JSON response
      // Extract latitude and longitude from each data item and store in arcsData

      let response = await webresponse.json();
      console.log(response);
      arcsData = [];
      for (let i = 0; i < response.length; i++) {
        let item = response[i];
        console.log(item);
        if (item.latitude == "" || item.longitude == "") {
          continue;
        }
        arcsData.push({
          startLat: latitude,
          startLng: longitude,
          endLat: item.latitude,
          endLng: item.longitude,
          color: "red",
        });
      }
      console.log(arcsData);
      // Update the earth arcs data
    } catch (err) {
      error = err.message;
      console.log(error);
      console.log(response);
    } finally {
      loading = false;
    }
  }

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
        },
      );
    } else {
      errorMessage = "Geolocation is not supported by this browser.";
    }
  }

  // Call the function to get coordinates when the component is mounted
  import { onMount } from "svelte";
  onMount(getCoordinates);
  $: {
    if (latitude !== 0 && longitude !== 0) {
      fetchData(); // Fetch new data when geolocation is updated
    }
  }
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
<Earth bind:arcsData />

<style>
  .timestamp-container {
    position: absolute;
    display: flex;
    justify-content: space-between;
    z-index: 10;
    align-items: center;
    padding: 20px;
  }
  .left {
    padding-right: 10%;
    padding-left: 8%;
  }
  .right {
    padding-right: 10%;
    padding-left: 150%;
  }

  .timestamp-container > * {
    flex: 0 1 auto;
    font-size: 1.2em;
  }
</style>
