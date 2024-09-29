// JavaScript to add interactivity
document.addEventListener("DOMContentLoaded", function () {
    const textarea = document.querySelector("textarea");
    
    // Increase textarea size on focus
    textarea.addEventListener("focus", function () {
        this.style.height = "150px";
    });

    // Revert textarea size on blur
    textarea.addEventListener("blur", function () {
        this.style.height = "100px";
    });
});
