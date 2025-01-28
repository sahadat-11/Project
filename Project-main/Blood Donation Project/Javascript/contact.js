document.addEventListener("DOMContentLoaded", () => {
    const contactForm = document.querySelector("form");
    contactForm.addEventListener("submit", async (event) => {
        event.preventDefault();

        const formData = new FormData(contactForm);
        const data = new URLSearchParams();
        formData.forEach((value, key) => {
            data.append(key, value);
        });

        try {
            const response = await fetch("http://127.0.0.1:5000/contact", {
                method: "POST",
                body: data,
            });

            const result = await response.json();
            if (response.status === 200) {
                alert("Your message has been sent successfully!");
                contactForm.reset(); // Reset form after successful submission
            } else {
                alert(result.error);
            }
        } catch (error) {
            alert("An error occurred while sending the message.");
            console.error(error);
        }
    });
});
