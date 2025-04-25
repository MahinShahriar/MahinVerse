function toggleDarkMode() {
    const html = document.documentElement;
    const isDark = html.classList.toggle('dark');
    localStorage.setItem('darkMode', isDark);

    // Update ARIA attributes
    const toggle = document.querySelector('[role="switch"]');
    if (toggle) toggle.setAttribute('aria-checked', isDark);
}


const platformSelect = document.getElementById('platform');
var phoneNumberInput = document.getElementById('number');
var countryField = document.getElementById('country');


// Function to enable or disable phone number input based on platform selection
platformSelect.addEventListener('change', function() {

        if (platformSelect.value) {
            countryField.disabled = false;
            countryField.required = true;

            countryField.addEventListener('change', function(){

                if (countryField.value){
                    phoneNumberInput.required = true;
                    phoneNumberInput.disabled = false; // Enable the phone number input
                    phoneNumberInput.placeholder = 'Enter '+ platformSelect.value + ' number !';

                } else {
                     phoneNumberInput.value = "";
                     phoneNumberInput.required = false;
                     phoneNumberInput.disabled = true;  // Disable the phone number input
                }
            })

        } else {
            countryField.value = "";
            phoneNumberInput.value = "";
            phoneNumberInput.placeholder = "";
            countryField.disabled = true;
            countryField.required = false;

        };
});
if (platformSelect.value) {
        countryField.disabled = false;
        countryField.required = true;
    };

// function for success message in navbar
document.addEventListener("DOMContentLoaded", function () {
    const alertBox = document.getElementById("nav-alert");
    const closeButton = document.getElementById("close-alert");

    if (closeButton && alertBox) { // Corrected logical operator
        // Close button functionality
        closeButton.addEventListener("click", function () {
            alertBox.classList.add("opacity-0", "-translate-y-2");
            setTimeout(() => alertBox.remove(), 300); // Delay removal for smooth animation
        });
    }
});

// Function for animation in contact submit button
document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    const sendBtn = document.getElementById("send-btn");
    const btnText = document.getElementById("btn-text");
    const loadingSpinner = document.getElementById("loading-spinner");

    form.addEventListener("submit", function (event) {



        event.preventDefault(); // Prevent immediate form submission

        // Show loading animation inside button
        btnText.textContent = "Sending...";
        loadingSpinner.classList.remove("hidden");

        // Disable button to prevent multiple clicks
        sendBtn.disabled = true;
        sendBtn.classList.add("opacity-50", "cursor-not-allowed");

        // Wait 3 seconds, then submit form
        setTimeout(() => {
            form.submit(); // Submit the form after delay
        }, 3000);
    });
});