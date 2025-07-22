async function sendOTP() {
    const email = document.getElementById("email").value;
    if (!email) {
        alert("Please enter your email");
        return;
    }

    try {
        const response = await fetch('http://127.0.0.1:5000/send-otp', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({email})
        });

        const result = await response.json();
        alert(result.message || result.error);
    } catch (error) {
        console.error("Error sending OTP:", error);
        alert("Failed to send OTP. Please try again.");
    }
}

async function verifyOTP() {
    const email = document.getElementById("email").value;
    const otp = document.getElementById("otp").value;

    if (!email || !otp) {
        alert("Please enter your email and OTP");
        return;
    }

    try {
        const response = await fetch('http://127.0.0.1:5000/verify-otp', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email, otp })
        });

        const result = await response.json();
        alert(result.message || result.error);

        if (response.ok && result.message === "OTP verified successfully") {
            localStorage.setItem("email",email)
            window.location.href = "forgot_password.html"; // Redirect on successful OTP verification
        }
    } catch (error) {
        console.error("Error verifying OTP:", error);
        alert("Failed to verify OTP. Please try again.");
    }
}
