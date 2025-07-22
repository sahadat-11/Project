document.addEventListener("DOMContentLoaded", () => {
    fetchRequests();
});

function fetchRequests() {
    fetch("http://127.0.0.1:5000/get-request-blood")
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                console.error("Error fetching data:", data.error);
                return;
            }
            populateTable(data.data);
        })
        .catch(error => console.error("Fetch error:", error));
}

function populateTable(requests) {
    const tableBody = document.getElementById("request-tbody");
    tableBody.innerHTML = "";
    
    requests.forEach((request, index) => {
        const row = document.createElement("tr");

        row.innerHTML = `
            <td>${index + 1}</td>
            <td>${request.name}</td>
            <td>${request.blood_group}</td>
            <td>${request.no_of_bags}</td>
            <td><a href="tel:${request.mobile_number}">${request.mobile_number}</a></td>
            <td>${new Date(request.donation_date).toLocaleString()}</td>
            <td>${request.cause}</td>
            <td>${request.division}</td>
            <td>${request.district}</td>
            <td>${request.upazila}</td>
            <td>${request.hospital}</td>
        `;

        tableBody.appendChild(row);
    });
}