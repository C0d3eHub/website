
    document.addEventListener("DOMContentLoaded", function () {
        fetch('/update-counter/')
            .then(response => response.json())
            .then(data => {
                document.getElementById('visitor-counter').innerText = data.count;
            })
            .catch(error => {
                console.error("Error fetching visitor count:", error);
                document.getElementById('visitor-counter').innerText = "Error";
            });
    });

