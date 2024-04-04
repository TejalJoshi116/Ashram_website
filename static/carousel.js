// carousel.js

document.addEventListener('DOMContentLoaded', function() {
    let currentSlide = 0;
    const slides = document.querySelectorAll('.slide');
    const totalSlides = slides.length;

    function showSlide(n) {
        slides.forEach(slide => {
            slide.style.display = 'none';
        });

        if (n < 0) {
            currentSlide = totalSlides - 1;
        } else if (n >= totalSlides) {
            currentSlide = 0;
        } else {
            currentSlide = n;
        }

        slides[currentSlide].style.display = 'block';
    }

    function nextSlide() {
        showSlide(currentSlide + 1);
    }

    function prevSlide() {
        showSlide(currentSlide - 1);
    }

    // Show the first slide initially
    showSlide(currentSlide);

    // Automatically advance to the next slide every 5 seconds
    setInterval(nextSlide, 5000);
});
