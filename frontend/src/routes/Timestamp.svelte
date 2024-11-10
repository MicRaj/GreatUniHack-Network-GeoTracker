<script>
  // Props
  export let epochTime; // Epoch timestamp in seconds

  // Convert the epoch time to a Date object
  let dateTime;

  // Function to update the dateTime
  $: dateTime = new Date(epochTime * 1000);

  // Format date and time as DD-MM-YYYY, HH:MM:SS
  $: formattedDate = dateTime.toLocaleDateString("en-GB"); // Format as DD-MM-YYYY
  $: formattedTime = dateTime.toLocaleTimeString("en-GB", {
    hour: "2-digit",
    minute: "2-digit",
    second: "2-digit",
  });
</script>

<div class="datetime-display">
  <p>{formattedDate}, {formattedTime}</p>
</div>

<style>
  .datetime-display {
    font-family: DepartureMono-Regular, monospace;
    margin: 10%;
    text-wrap: nowrap;
    color: white;
  }
  .datetime-display p {
    margin: 0.5em 0;
    font-size: 1.2em;
  }
</style>
