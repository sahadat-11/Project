// Toggle Profile Dropdown
const profileDropdown = document.getElementById('footer-profile');
const userBtn = document.getElementById('user-btn');

userBtn.addEventListener('click', () => {
    profileDropdown.classList.toggle('active');
});


let body= document.body;
document.addEventListener("DOMContentLoaded",async()=>{
    console.log("inside the load function...")
    const div=document.getElementById("sidebar-profile");
    const div2=document.getElementById("header-profile");
    const div3=document.getElementById("main-profile");
    if(localStorage.getItem("id")){
        const res=await fetch(`http://127.0.0.1:5000/user/${localStorage.getItem("id")}`)
        const data=await res.json()
        console.log(data)
        div.innerHTML=`
            <img src='${data['data']['image']}'>
            <!-- need to add data['data']base -->
            <h3>${data['data']['name']}</h3>
            <!--<span>Donor</span> -->
            <a href="Profile.html" class="btn">Viewprofile</a>
        `
        div2.innerHTML=`
            <img src='${data['data']['image']}'>
                <!-- need to add data['data']base -->
                <h3>${data['data']['name']}</h3>
                <!--<span>Donor</span> -->
                <a href="Profile.html" class="btn">Viewprofile</a>

                <div class="flex-btn">
                    <a href="update.html" class="option-btn">Update Profile</a>
                </div>
                <div class="flex-btn">
                    <a href="change_password.html" class="option-btn">Change Password</a>
                </div>
        `
        div3.innerHTML = `<img src='${data['data']['image'] || "default-image.png"}' alt="Profile Image" style="max-width: 100px; border-radius: 50%;">
        <table border="1" style="width: 100%; text-align: left; margin-top: 20px; border-collapse: collapse;">
        <tr>
            <th>Field</th>
            <th>Value</th>
        </tr>
        <tr>
            <td>Username</td>
            <td>${data['data']['name'] || "N/A"}</td>
        </tr>
        <tr>
            <td>Email</td>
            <td>${data['data']['email'] || "N/A"}</td>
        </tr>
        <tr>
            <td>Mobile Number</td>
            <td>${data['data']['mobile_number'] || "N/A"}</td>
        </tr>
        <tr>
            <td>Division</td>
            <td>${data['data']['division'] || "Not specified"}</td>
        </tr>
        <tr>
            <td>District</td>
            <td>${data['data']['district'] || "Not specified"}</td>
        </tr>
        <tr>
            <td>Upazila</td>
            <td>${data['data']['upazila'] || "Not specified"}</td>
        </tr>
        <tr>
            <td>Last Donation Date</td>
            <td>${data['data']['last_donate'] || "Not specified"}</td>
        </tr>
        <tr>
            <td>Registration Date</td>
            <td>${data['data']['registration_date'] || "Not specified"}</td>
        </tr>
        </table>
        <a href="update.html" class="btn" style="display: block; margin-top: 20px; text-align: center;">Update Profile</a>`

    }
})

let prof = document.querySelector('.header .flex .profile');
document.querySelector('#user-btn').onclick = () =>{
    prof.classList.toggle('active');
    search.classList.remove('active');

}


let search = document.querySelector('header .flex .search-form');
document.querySelector('#search-btn').onclick = () =>{
    // search.classList.toggle('active');
    prof.classList.remove('active');
}

let side = document.querySelector('.sidebar');
document.querySelector('#menu-btn').onclick = () =>{
    side.classList.toggle('active');
    body.classList.toggle('active');
}
document.querySelector('.sidebar .close-sidebar').onclick =() =>{
                      
    side.classList.toggle('active');
    body.classList.toggle('active');
     
}


document.querySelector(' .close-sidebar').onclick =() =>{
    side.classList.remove('active');
    body.classList.remove('active');
 
}
