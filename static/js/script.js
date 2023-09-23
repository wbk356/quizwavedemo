document.addEventListener("DOMContentLoaded", function () {
    const popup = document.getElementById("popup");
    const closePopup = document.getElementById("close-popup");
    const okButton = document.getElementById("ok-button");

    // Show the popup when the page loads
    popup.style.display = "block";

    // Close the popup when the close button is clicked
    closePopup.addEventListener("click", function () {
        popup.style.display = "none";
    });

    // Close the popup when clicking outside the content
    window.addEventListener("click", function (event) {
        if (event.target === popup) {
            popup.style.display = "none";
        }
    });

    // Close the popup when the "OK" button is clicked
    okButton.addEventListener("click", function () {
        popup.style.display = "none";
    });
});
