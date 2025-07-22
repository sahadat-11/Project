document.getElementById("change_password").addEventListener("submit", async (event) => {
    event.preventDefault();

    const form = event.target;
    const currentPassword = form.querySelector("input[name='password']").value.trim();
    const newPassword = form.querySelector("input[name='new_pass']").value.trim();
    const confirmPassword = form.querySelector("input[name='con_pass']").value.trim();

    if (!currentPassword || !newPassword || !confirmPassword) {
        alert("All fields are required.");
        return;
    }

    if (newPassword !== confirmPassword) {
        alert("New password and confirm password do not match.");
        return;
    }

    const formData = new FormData();
    formData.append("password", currentPassword);
    formData.append("new_pass", newPassword);

    try {
        const res = await fetch(`http://127.0.0.1:5000/change-password/${localStorage.getItem("id")}`, {
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
