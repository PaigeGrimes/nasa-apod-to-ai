// JavaScript to get API information
    var req = new XMLHttpRequest();
    var url = "https://api.nasa.gov/planetary/apod?api_key=";
    var api_key = "APOD_KEY";

    req.open("GET", url + api_key, true);
    req.send();

    req.addEventListener("load", function(){
    if(req.status == 200 && req.readyState == 4) {
        var response = JSON.parse(req.responseText);
        var title = response.title;
        var date = response.date;
        var pic = response.hdurl;

        document.getElementById("title").textContent = response.title;
        document.getElementById("date").textContent = response.date;
        document.getElementById("pic").src = response.hdurl;

        // Store the explanation in a variable
        var explanationText = response.explanation;
        var url = '/submit?' +
            'title=' + encodeURIComponent(title) +
            '&date=' + encodeURIComponent(date) +
            '&pic=' + encodeURIComponent(pic) +
            '&explanation=' + encodeURIComponent(explanationText);

        // Set the explanation content
        document.getElementById("explanation").textContent = explanationText;

        // Call fetchGPT with the stored explanation
        fetchGPT(url, function(imageUrl) {
            // Update image source using the provided URL
            document.getElementById("yourImageElementId").src = imageUrl;
        });
    }
});

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