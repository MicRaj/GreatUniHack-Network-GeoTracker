<script>
    export let marker1Position = 0;
    export let marker2Position = 0;


    let dragMarker = null;
    let timelineWidth = 1500; // Timeline width
  
    let timelineRect;

    function handleDrag(e) {
        if (dragMarker) {
            // Calculate position using the stored timelineRect
            const newPos = Math.min(
                Math.max(e.clientX - timelineRect.left, 0),
                timelineWidth
            );

            // Prevent markers from crossing each other
            if (dragMarker === 'marker1' && newPos < marker2Position) {
                marker1Position = newPos;
            } else if (dragMarker === 'marker2' && newPos > marker1Position) {
                marker2Position = newPos;
            }
        }
    }

    function startDrag(e, marker) {
        dragMarker = marker;

        // Store the timeline container's bounding rectangle once when dragging starts
        timelineRect = e.target.closest('.timeline-container').getBoundingClientRect();
        console.log(timelineRect);
        document.addEventListener('mousemove', handleDrag);
        document.addEventListener('mouseup', stopDrag);
    }
  
    function stopDrag() {
      dragMarker = null;
      document.removeEventListener('mousemove', handleDrag);
      document.removeEventListener('mouseup', stopDrag);
    }
  </script>
  
  <style>
    .timeline-container {
      position: relative;
      width: 1500px;
      height: 30px;
      background-color: #e0e0e0;
      border-radius: 5px;
    }
  
    .timeline-line {
      position: absolute;
      top: 50%;
      left: 0;
      right: 0;
      height: 2px;
      background-color: #333;
      transform: translateY(-50%);
    }
  
    .marker {
      position: absolute;
      top: 50%;
      width: 8px;
      height: 20px;
      background-color: #007BFF;
      border-radius: 25%;
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
  
  <div class="timeline-container" >
    <div class="timeline-line"></div>
    
    <!-- Updated: Added role="slider" and replaced on:mousedown with onmousedown -->
    <div
      class="marker marker1"
      role="slider"
      aria-valuemin="0"
      aria-valuemax="500"
      aria-valuenow="{marker1Position}"
      style="--marker1-position: {marker1Position}px;"
      onmousedown={(e) => startDrag(e, 'marker1')}
      tabindex="0"
    ></div>
  
    <div
      class="marker marker2"
      role="slider"
      aria-valuemin="0"
      aria-valuemax="500"
      aria-valuenow="{marker2Position}"
      style="--marker2-position: {marker2Position}px;"
      onmousedown={(e) => startDrag(e, 'marker2')}
      tabindex="0"
    ></div>
  </div>
  
  