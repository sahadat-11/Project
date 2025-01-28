document.addEventListener("DOMContentLoaded", () => {
    data = JSON.parse(localStorage.getItem("donors_info"));
    data.forEach(item => console.log(item));
    
    populateTable(data);
});

function populateTable(donors) {
    const tableBody = document.getElementById("donor-tbody");
    tableBody.innerHTML = "";
    
    donors.forEach(donor => {
        const row = document.createElement("tr");
        
        const nameCell = document.createElement("td");
        nameCell.textContent = donor.name;
        
        const mobileCell = document.createElement("td");
        const mobileLink = document.createElement("a");
        mobileLink.href = `tel:${donor.mobile_number}`;
        mobileLink.textContent = donor.mobile_number;
        mobileCell.appendChild(mobileLink); 
        
        const bloodGroupCell = document.createElement("td");
        bloodGroupCell.textContent = donor.blood_group;

        const divisionCell = document.createElement("td");
        divisionCell.textContent = donor.division;

        const districtCell = document.createElement("td");
        districtCell.textContent = donor.district;

        const upazilaCell = document.createElement("td");
        upazilaCell.textContent = donor.upazila;

        const lastdonationCell = document.createElement("td");
        lastdonationCell.textContent = donor.last_donate;

        row.appendChild(nameCell);
        row.appendChild(mobileCell);
        row.appendChild(bloodGroupCell);
        row.appendChild(divisionCell);
        row.appendChild(districtCell);
        row.appendChild(upazilaCell);
        row.appendChild(lastdonationCell);
        
        tableBody.appendChild(row);
    });
}
