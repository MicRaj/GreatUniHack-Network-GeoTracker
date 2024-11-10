<script>
  export let timelineWidth;

  export let marker1Position = 0;
  export let marker2Position = timelineWidth;

  export let normPos1 = marker1Position / timelineWidth;
  export let normPos2 = marker2Position / timelineWidth;

  export let sendGetRequest;

  let previosMarker1Position = marker1Position;
  let previosMarker2Position = marker2Position;

  let dragMarker = null;
  let timelineRect;

  function handleDrag(e) {
    if (dragMarker) {
      // Calculate position using the stored timelineRect
      const newPos = Math.min(
        Math.max(e.clientX - timelineRect.left, 0),
        timelineWidth
      );

      // Prevent markers from crossing each other
      if (dragMarker === "marker1" && newPos < marker2Position) {
        marker1Position = newPos;
        normPos1 = marker1Position / timelineWidth;
      } else if (dragMarker === "marker2" && newPos > marker1Position) {
        marker2Position = newPos;
        normPos2 = marker2Position / timelineWidth;
      }
    }
  }

  function startDrag(e, marker) {
    dragMarker = marker;

    // Store the timeline container's bounding rectangle once when dragging starts
    timelineRect = e.target
      .closest(".timeline-container")
      .getBoundingClientRect();
    console.log(timelineRect);
    document.addEventListener("mousemove", handleDrag);
    document.addEventListener("mouseup", stopDrag);
  }

  function stopDrag() {
    dragMarker = null;
    document.removeEventListener("mousemove", handleDrag);
    document.removeEventListener("mouseup", stopDrag);
    // If the marker position has changed GET request to the server
    if (
      previosMarker1Position !== marker1Position ||
      previosMarker2Position !== marker2Position
    ) {
      sendGetRequest();
      previosMarker1Position = marker1Position;
      previosMarker2Position = marker2Position;
    }
  }
</script>

<div class="center-wrapper">
  <div
    class="timeline-container"
    style="width: {parseInt(timelineWidth) + 8}px"
  >
    <div class="timeline-line"></div>
    <!-- Active line between markers -->
    <div
      class="active-line"
      style="left: {marker1Position}px; width: {marker2Position -
        marker1Position}px;"
    ></div>
    <!-- Updated: Added role="slider" and replaced on:mousedown with onmousedown -->
    <div
      class="marker marker1"
      role="slider"
      aria-valuemin="0"
      aria-valuemax={timelineWidth}
      aria-valuenow={marker1Position}
      style="--marker1-position: {marker1Position}px;"
      onmousedown={(e) => startDrag(e, "marker1")}
      tabindex="0"
    ></div>

    <div
      class="marker marker2"
      role="slider"
      aria-valuemin="0"
      aria-valuemax={timelineWidth}
      aria-valuenow={marker2Position}
      style="--marker2-position: {marker2Position}px;"
      onmousedown={(e) => startDrag(e, "marker2")}
      tabindex="0"
    ></div>
  </div>
</div>

<style>
  .center-wrapper {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
  }

  .timeline-container {
    position: relative;
    width: 100%;
    height: 30px;
    background-color: #141111;
    border-radius: 1px;
  }

  .timeline-line {
    position: absolute;
    top: 50%;
    left: 0;
    right: 0;
    height: 4px;
    background-color: #ffffff;
    transform: translateY(-50%);
  }
  /* Active line style */
  .active-line {
    position: absolute;
    top: 50%;
    height: 5px;
    background-color: #ff4f00; /* Distinct color for the line between markers */
    transform: translateY(-50%);
  }

  .marker {
    position: absolute;
    top: 50%;
    width: 8px;
    height: 20px;
    background-color: #ffaf8b;
    cursor: pointer;
    transform: translateY(-50%);
    user-select: none;
  }

  .marker1 {
    left: var(--marker1-position);
  }

  .marker2 {
    left: var(--marker2-position);
  }
</style>
