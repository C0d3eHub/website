// Get the scroll to top button
var scrollToTopBtn = document.getElementById("scrollToTop");

// Show the button when the user scrolls down 100px from the top
window.onscroll = function() {
    console.log("Scrolling..."); // Log when scrolling happens
    if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
        scrollToTopBtn.style.display = "block"; // Show the button
        console.log("Button shown"); // Log button show
    } else {
        scrollToTopBtn.style.display = "none";  // Hide the button
        console.log("Button hidden"); // Log button hide
    }
};
