    const handleSearchBlood=() =>{
        if(localStorage.getItem("id")){
            window.location.href="../HTML/search.html";
        }
        else{
            window.location.href="../HTML/login.html";
        }
    }

    document.addEventListener("DOMContentLoaded", function () {
        // Set default values
        if(localStorage.getItem("id")){
            document.getElementById('login-menu').style.display='none';
            document.getElementById('logout-menu').style.display='block';
        }
        else{
            document.getElementById('logout-menu').style.display='none';
            document.getElementById('login-menu').style.display='block';
        }
    });

    const handleLogout= () =>{
        localStorage.removeItem("id")
        window.location.href="../HTML/home.html"
    }



































    // document.addEventListener('DOMContentLoaded', function() {
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
//         console.log(side.classList); 
//     }   

//     // document.querySelector('.sidebar .close-sidebar').onclick =() =>{
//     //     side.classList.remove('active');
//     //     body.classList.remove('active');
//     // }

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

//            // toggle button eikhane
//     let toggleBtn = document.querySelector('#toggle-btn');
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
