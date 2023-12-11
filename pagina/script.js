document.getElementById('parameter-form').addEventListener('submit', function(e) {
    e.preventDefault();

    // Get parameter values from the form
    var volumeFraction = document.getElementById('volume-fraction').value;
    var radius = document.getElementById('radio').value;
    var filmThickness = document.getElementById('thickness').value;

    // Prepare data to be sent
    var data = {
        volumeFraction: volumeFraction,
        radius: radius,
        filmThickness: filmThickness
    };

    // Send the parameters to the Flask server
    fetch('http://localhost:5000/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        // Display the result image
        var img = document.getElementById('result-image');
        img.src = 'data:image/png;base64,' + data.image;
        img.style.display = 'block';
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});
