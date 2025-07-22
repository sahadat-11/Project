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
            console.log("Upcoming Requests:", data.data);  // Debugging
            populateTable(data.data);
        })
        .catch(error => console.error("Fetch error:", error));
}

function populateTable(requests) {
    const tableBody = document.getElementById("request-tbody");
    tableBody.innerHTML = "";  // Clear table before populating

    if (requests.length === 0) {
        console.log("No upcoming requests found");
        return;
    }

    // Group requests by blood group
    const groupedRequests = groupByBloodGroup(requests);

    // Loop through each blood group and create a table section for it
    Object.keys(groupedRequests).forEach(bloodGroup => {
        const groupRequests = groupedRequests[bloodGroup];

        // Add a section header for each blood group
        const groupHeader = document.createElement("tr");
        groupHeader.innerHTML = `<th colspan="9">Blood Group: ${bloodGroup}</th>`;
        tableBody.appendChild(groupHeader);

        // Add rows for each request within this blood group
        groupRequests.forEach((request, index) => {
            console.log("Request Data:", request);  // Debugging

            const location = `${request.upazila}, ${request.district}, ${request.division}`;

            const row = document.createElement("tr");
            row.innerHTML = `
                <td>${index + 1}</td>
                <td>${request.name}</td>
                <td>${request.blood_group}</td>
                <td>${request.no_of_bags}</td>
                <td><a href="tel:${request.mobile_number}">${request.mobile_number}</a></td>
                <td>${new Date(request.donation_date).toLocaleString()}</td>
                <td>${request.cause}</td>
                <td>${request.hospital}</td>
                <td>${location}</td> 
            `;

            tableBody.appendChild(row);
        });
    });
}

// Group requests by blood group
function groupByBloodGroup(requests) {
    return requests.reduce((grouped, request) => {
        const bloodGroup = request.blood_group;
        if (!grouped[bloodGroup]) {
            grouped[bloodGroup] = [];
        }
        grouped[bloodGroup].push(request);
        return grouped;
    }, {});
}
