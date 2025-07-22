document.addEventListener("DOMContentLoaded", () => {
    let data = JSON.parse(localStorage.getItem("donors_info")) || [];
    
    // Check if data exists
    if (data.length === 0) {
        console.log("No donor data found.");
        return;
    }

    populateTable(data);
});

function populateTable(donors) {
    const tableBody = document.getElementById("donor-tbody");
    tableBody.innerHTML = "";
    
    donors.forEach((donor, index) => {
        const row = document.createElement("tr");
        
        // Serial number column (No)
        const serialCell = document.createElement("td");
        serialCell.textContent = index + 1; // Start from 1
        row.appendChild(serialCell);

        // Name column
        const nameCell = document.createElement("td");
        nameCell.textContent = donor.name;
        row.appendChild(nameCell);

        // Mobile column (with clickable link)
        const mobileCell = document.createElement("td");
        const mobileLink = document.createElement("a");
        mobileLink.href = `tel:${donor.mobile_number}`;
        mobileLink.textContent = donor.mobile_number;
        mobileCell.appendChild(mobileLink);
        row.appendChild(mobileCell);

        // Blood Group column
        const bloodGroupCell = document.createElement("td");
        bloodGroupCell.textContent = donor.blood_group;
        row.appendChild(bloodGroupCell);

        // Division column
        const divisionCell = document.createElement("td");
        divisionCell.textContent = donor.division;
        row.appendChild(divisionCell);

        // District column
        const districtCell = document.createElement("td");
        districtCell.textContent = donor.district;
        row.appendChild(districtCell);

        // Upazila column
        const upazilaCell = document.createElement("td");
        upazilaCell.textContent = donor.upazila;
        row.appendChild(upazilaCell);

        // Last Donation Date column
        const lastDonationCell = document.createElement("td");
        lastDonationCell.textContent = donor.last_donate;
        row.appendChild(lastDonationCell);

        tableBody.appendChild(row);
    });
}
