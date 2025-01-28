const my_form = document.getElementById("login-form")
console.log("register page")
my_form.addEventListener('submit', function(event){
    event.preventDefault()
    const form = event.target
    const payload = new FormData(form)
    console.log(payload)
    fetch_api(payload)
})

const fetch_api =async payload =>{
    const res=await fetch('http://127.0.0.1:5000/login',{
        method: "POST",
        body: payload
    }
    );
    const data=await res.json();
    console.log(data)
    if(!data['error']){
        localStorage.setItem("id",data['data']['id'])
        localStorage.setItem("image",data['data']['image'])
        localStorage.setItem("name",data['data']['name'])
        window.location.href="../HTML/home.html"
    }
}