const my_form = document.getElementById("login-form")
console.log("register page")
my_form.addEventListener('submit', function(event){
    event.preventDefault()
    const form = event.target
    const payload = new FormData(form)
    console.log(payload)
    fetch_api(payload)
})

const fetch_api = async (payload) => {
    try {
        const res = await fetch('http://127.0.0.1:5000/login', {
            method: "POST",
            body: payload,
        });

        const data = await res.json();

        if (res.ok) {
            
            localStorage.setItem("id", data["data"]["id"]);
            localStorage.setItem("image", data["data"]["image"]);
            localStorage.setItem("name", data["data"]["name"]);
            window.location.href = "../HTML/home.html";
        } else {
            
            if (res.status === 404) {
                alert("Email not found. Please check your email or register.");
            } else if (res.status === 401) {
                alert("Incorrect password. Please try again.");
            } else {
                alert(data.error || "An unknown error occurred.");
            }
        }
    } catch (error) {
        console.error("Error logging in:", error);
        alert("Unable to connect to the server. Please try again later.");
    }
};
