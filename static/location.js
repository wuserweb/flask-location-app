window.onload = function () {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(
      function (position) {
        // User allowed location access
        const lat = position.coords.latitude;
        const lon = position.coords.longitude;
        const accuracy = position.coords.accuracy;

        console.log("User location:", lat, lon, "Accuracy (m):", accuracy);

        // Send location to backend
        fetch("/location", {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({ latitude: lat, longitude: lon, accuracy: accuracy })
        })
        .then(response => response.json())
        .then(data => {
          console.log("Server response:", data);
        })
        .catch(error => {
          console.error("Error sending location:", error);
        });
      },
      function (error) {
        // User denied or error
        console.warn("Geolocation error:", error.message);
      }
    );
  } else {
    alert("Geolocation is not supported by this browser.");
  }
};
