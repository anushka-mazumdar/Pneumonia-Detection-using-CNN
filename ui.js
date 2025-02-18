document.addEventListener('DOMContentLoaded', function() {
    const uploadForm = document.getElementById('uploadForm');
    const fileInput = document.getElementById('fileInput');
    const resultDiv = document.getElementById('result');

    uploadForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const formData = new FormData();
        formData.append('file', fileInput.files[0]);

        fetch('http://localhost:5000/predict', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            resultDiv.innerHTML = `<p>Prediction: ${data.prediction}</p>`;
        })
        .catch(error => {
            console.error('Error:', error);
            resultDiv.innerHTML = `<p>Error: ${error.message}</p>`;
        });
    });
});