// import {data} from "./search"
document.addEventListener("DOMContentLoaded", () => {
    // fetchDonors();
    data=JSON.parse(localStorage.getItem("donors_info"))
    data.forEach(item=>console.log(item))
    
    populateTable(data)
});



function populateTable(donors) {
    const tableBody = document.getElementById("donor-tbody");
    tableBody.innerHTML = ""; // Clear any existing rows
    
    donors.forEach(donor => {
        const row = document.createElement("tr");
        
        const nameCell = document.createElement("td");
        nameCell.textContent = donor.name;
        
        const mobileCell = document.createElement("td");
        mobileCell.textContent = donor.mobile_number;
        
        const bloodGroupCell = document.createElement("td");
        bloodGroupCell.textContent = donor.blood_group;

        const divisioncell=document.createElement("td")
        divisioncell.textContent=donor.division
        const districtcell=document.createElement("td")
        districtcell.textContent=donor.district
        const upazilacell=document.createElement("td")
        upazilacell.textContent=donor.upazila

        row.appendChild(nameCell);
        row.appendChild(mobileCell);
        row.appendChild(bloodGroupCell);
        row.appendChild(divisioncell);
        row.appendChild(districtcell);
        row.appendChild(upazilacell);
        tableBody.appendChild(row);
    });
}
