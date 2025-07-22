document.getElementById("forgot_password").addEventListener("submit", async (event) => {
    event.preventDefault();
    const form=event.target
    const newPass = form.querySelector("input[name='new_pass']").value.trim();
    const conPass = form.querySelector("input[name='con_pass']").value.trim();

    if (newPass !== conPass) {
        alert("Passwords do not match");
        return;
    }

    const formData = new FormData(event.target);
    formData.set("new_pass", newPass);
    formData.append("email",localStorage.getItem("email"))
    try {
        const res = await fetch(`http://127.0.0.1:5000/forgot-password`, {
            method: "POST",
            body: formData,
        });

        const data = await res.json();

        if (!res.ok) {
            alert(data.error || "Failed to change the password. Please try again.");
            return;
        }

        alert("Password changed successfully!");
        window.location.href = "../HTML/login.html"; // Redirect after password change
    } catch (error) {
        console.error("Error:", error);
        alert("Something went wrong. Please try again.");
    }
});
