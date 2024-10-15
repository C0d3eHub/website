let slideIndex = 1;
let slideInterval;

// Function to show slides
function showSlides(n) {
    let slides = document.querySelectorAll('.slider img');
    let dots = document.querySelectorAll('.dot');

    if (n > slides.length) { slideIndex = 1; }
    if (n < 1) { slideIndex = slides.length; }

    // Hide all slides
    slides.forEach((slide, index) => {
        slide.style.display = (index === slideIndex - 1) ? "block" : "none"; // Show current slide
    });

    // Remove the "active" class from all dots and add it to the current dot
    dots.forEach((dot, index) => {
        dot.classList.remove("active");
        if (index === slideIndex - 1) {
            dot.classList.add("active");
        }
    });
}

// Function to move to the next slide
function showNextImage() {
    showSlides(slideIndex += 1);
}

// Function to move to the previous slide
function showPreviousImage() {
    showSlides(slideIndex -= 1);
}

// Function to display a specific slide based on the dot clicked
function currentSlide(n) {
    showSlides(slideIndex = n);
}

// Function to start automatic slideshow
function startSlideShow() {
    slideInterval = setInterval(() => {
        showNextImage(); // Move to the next slide every 5 seconds
    }, 5000); // 5000 milliseconds = 5 seconds
}

// Function to stop the automatic slideshow when needed (optional)
function stopSlideShow() {
    clearInterval(slideInterval);
}

// Start the slideshow once the document is fully loaded
document.addEventListener("DOMContentLoaded", function() {
    showSlides(slideIndex); // Show the first slide
    startSlideShow(); // Start the automatic slideshow
});
