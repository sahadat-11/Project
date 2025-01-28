let body= document.body;
document.addEventListener("DOMContentLoaded",()=>{
    console.log("inside the load function...")
    const div=document.getElementById("sidebar-profile");
    const div2=document.getElementById("header-profile")
    if(localStorage.getItem("id")){
        div.innerHTML=`
            <img src='${localStorage.getItem("image")}'>
            <!-- need to add database -->
            <h3>${localStorage.getItem("name")}</h3>
            <span>Donor</span>
            <a href="Profile.html" class="btn">Viewprofile</a>
        `
        div2.innerHTML=`
            <img src='${localStorage.getItem("image")}'>
                <!-- need to add database -->
                <h3>${localStorage.getItem("name")}</h3>
                <span>Donor</span>
                <a href="Profile.html" class="btn">Viewprofile</a>

                <div class="flex-btn">
                    <a href="Login.html" class="option-btn">Login</a>
                    <a href="Register.html" class="delete-btn">Register</a>
                </div>
        `
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


console.log("ideclassList");

window.onscroll = () =>{
    prof.classList.remove('active');
    // search.classList.remove('active');
    if(innerWidth<1200){
        side.classList.remove('active');
        body.classList.remove('active');
    }
}

// toggle button eikhane
let toggleBtn = document.querySelector('#toggle-btn');
let darkMode = localStorage.getItem('dark-mode');
// body = document.querySelector('body');


const enableDarkMode = () => {
    toggleBtn.classList.replace('fa-sun', 'fa-moon');
    body.classList.add('dark');
    localStorage.setItem('dark-mode', 'enabled');
};

const disableDarkMode = () => {
    toggleBtn.classList.replace('fa-moon', 'fa-sun');
    body.classList.remove('dark');
    localStorage.setItem('dark-mode', 'disabled');
};

if (darkMode === 'enabled') {
    enableDarkMode();
}

toggleBtn.onclick = () => {
    let darkMode = localStorage.getItem('dark-mode');
    if (darkMode === 'disabled') {
        enableDarkMode();
    } else {
        disableDarkMode();
    }
};  





//    // document.addEventListener('DOMContentLoaded', function() {
            //     let body=document.body;
            //     let prof = document.querySelector('.header .flex .profile');
            //     document.querySelector('#user-btn').onclick = () => {
            //         prof.classList.toggle('active');
            //         search.classList.remove('active');
            //     }
            //     let search = document.querySelector('header .flex .search-form');
            //     document.querySelector('#search-btn').onclick = () =>{
            //         search.classList.toggle('active');
            //         prof.classList.remove('active');
            //     }               
            //     let side = document.querySelector('.sidebar');
            //     document.querySelector('#menu-btn').onclick = () =>{
            //         side.classList.toggle('active');
            //         body.classList.toggle('active');
            //     }   
            //     document.querySelector('.sidebar .close-sidebar').onclick =() =>{
            //         side.classList.toggle('active');
            //         body.classList.toggle('active');
            //     }
             
            //     window.onscroll = () => {
            //         prof.classList.remove('active');
            //         search.classList.remove('active');
            //         if(innerWidth<1200){
            //             side.classList.remove('active');
            //             body.classList.remove('active');
            //         }
            //     }
            // });
            // let toggleBtn = document.querySelector('#toggle-btn');
            //     let darkMode = localStorage.getItem('dark-mode');
            //     let body = document.querySelector('body');

            //     const enableDarkMode = () => {
            //         toggleBtn.classList.replace('fa-sun', 'fa-moon');
            //         body.classList.add('dark');
            //         localStorage.setItem('dark-mode', 'enabled');
            //     };

            //     const disableDarkMode = () => {
            //         toggleBtn.classList.replace('fa-moon', 'fa-sun');
            //         body.classList.remove('dark');
            //         localStorage.setItem('dark-mode', 'disabled');
            //     };

            //     if (darkMode === 'enabled') {
            //         enableDarkMode();
            //     }

            //     toggleBtn.onclick = () => {
            //         let darkMode = localStorage.getItem('dark-mode');
            //         if (darkMode === 'disabled') {
            //             enableDarkMode();
            //         } else {
            //             disableDarkMode();
            //         }
            //     };  
