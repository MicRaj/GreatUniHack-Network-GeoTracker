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
