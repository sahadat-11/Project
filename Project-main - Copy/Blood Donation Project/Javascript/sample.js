let currentIndex = 0;
const slider = document.getElementById("slider");
const images = document.querySelectorAll("#slider img");
const totalImages = images.length;

function slideImages() {
  currentIndex++;
  if (currentIndex === totalImages) {
    currentIndex = 0;
  }
  slider.style.transform = `translateX(${-100 * currentIndex}%)`;
}

setInterval(slideImages, 2000); 