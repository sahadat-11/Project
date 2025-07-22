document.addEventListener("DOMContentLoaded", function () {
    const ticker = document.querySelector(".ticker");
    const clone = ticker.cloneNode(true); 
    ticker.parentNode.appendChild(clone);
});
