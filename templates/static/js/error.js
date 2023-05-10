// error.js
document.addEventListener("DOMContentLoaded", function() {
    var errorMessageElement = document.getElementById("error-message");
    var errorMessage = errorMessageElement.innerText.trim();  // Trim leading/trailing whitespace
    if (errorMessage.includes("Error")) {
      alert(errorMessage)
    }
}); 
