// js-api.js

// Initialize request variables
var req = new XMLHttpRequest();
var url = "https://api.nasa.gov/planetary/apod?api_key=";
var api_key = "DEMO_KEY";

// Get the API url and api_key
req.open("GET", url + api_key, true);
req.send();

req.addEventListener("load", function(){
    if(req.status === 200 && req.readyState === 4) {
        var response = JSON.parse(req.responseText);
        var title = response.title;
        var date = response.date;
        var pic = response.hdurl;

        document.getElementById("title").textContent = response.title;
        document.getElementById("date").textContent = response.date;
        document.getElementById("pic").src = response.hdurl;

        // Store the api data in a variable to pass it to the '/submit' route
        var explanationText = response.explanation;
        var url = '/submit?' +
            'title=' + encodeURIComponent(title) +
            '&date=' + encodeURIComponent(date) +
            '&pic=' + encodeURIComponent(pic) +
            '&explanation=' + encodeURIComponent(explanationText);

        // Set the explanation content
        document.getElementById("explanation").textContent = explanationText;

        // Call fetchGPT with the stored data - it will return an AI image and data will be stored in the database.
        fetchGPT(url, function(imageUrl) {
            // Update image source using the provided URL
            document.getElementById("yourImageElementId").src = imageUrl;
        });
    }
});

// Get the OpenAI image from app.py
function fetchGPT(url, callback) {
    const xhr = new XMLHttpRequest();

    // Use the new endpoint to fetch data
    xhr.open('GET', url, true);

    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            const responseJson = JSON.parse(xhr.responseText);
            const imageUrl = responseJson.image;
            callback(imageUrl);
        }
    };

    xhr.send();
}

// Allows users to refresh the webpage after clicking a button.
function refreshPage() {
    // Reloads the current page
    location.reload();
}