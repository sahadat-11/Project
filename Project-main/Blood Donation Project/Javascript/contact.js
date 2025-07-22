
document.getElementById("contactForm").addEventListener("submit", async function(event) {
    event.preventDefault(); // Prevent form submission

    let formData = new FormData(this);
    let mobileNumber = formData.get("mobile_number");

    // Check if mobile number starts with "01"
    if (!mobileNumber.startsWith("01")) {
        alert("Mobile number must start with '01'.");
        return;
    }

    // Check if mobile number has exactly 11 digits
    if (mobileNumber.length !== 11 || isNaN(mobileNumber)) {
        alert("Mobile number must be exactly 11 digits.");
        return;
    }

    try {
        let response = await fetch("http://127.0.0.1:5000/submit-contact", {
            method: "POST",
            body: formData
        });

        let result = await response.json();

        if (response.ok) {
            alert("Message sent successfully!");
            this.reset(); // Clear form
        } else {
            alert("Error: " + result.error);
        }
    } catch (error) {
        console.error("Error:", error);
        alert("An error occurred. Please try again.");
    }
});

