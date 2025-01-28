




document.addEventListener('DOMContentLoaded', () => {
  const divisionSelect = document.getElementById('division');
  const districtSelect = document.getElementById('district');
  const upazilaSelect = document.getElementById('upazila');

  // Fetch and populate divisions
  fetch('/api/divisions')
      .then(response => response.json())
      .then(data => {
          data.forEach(division => {
              const option = document.createElement('option');
              option.value = division.id;
              option.textContent = division.name;
              divisionSelect.appendChild(option);
          });
      });

  // Populate districts based on selected division
  divisionSelect.addEventListener('change', () => {
      const divisionId = divisionSelect.value;
      districtSelect.innerHTML = '<option value="">Select District</option>';
      upazilaSelect.innerHTML = '<option value="">Select Upazila</option>';

      fetch(`/api/districts/${divisionId}`)
          .then(response => response.json())
          .then(data => {
              data.forEach(district => {
                  const option = document.createElement('option');
                  option.value = district.id;
                  option.textContent = district.name;
                  districtSelect.appendChild(option);
              });
          });
  });

  // Populate upazilas based on selected district
  districtSelect.addEventListener('change', () => {
      const districtId = districtSelect.value;
      upazilaSelect.innerHTML = '<option value="">Select Upazila</option>';

      fetch(`/api/upazilas/${districtId}`)
          .then(response => response.json())
          .then(data => {
              data.forEach(upazila => {
                  const option = document.createElement('option');
                  option.value = upazila.id;
                  option.textContent = upazila.name;
                  upazilaSelect.appendChild(option);
              });
          });
  });

  // Submit form
  const form = document.getElementById('userForm');
  form.addEventListener('submit', (event) => {
      event.preventDefault();

      const formData = new FormData(form);
      fetch('/api/users', {
          method: 'POST',
          body: JSON.stringify(Object.fromEntries(formData)),
          headers: {
              'Content-Type': 'application/json'
          }
      })
      .then(response => response.json())
      .then(data => alert('User registered successfully!'))
      .catch(error => console.error('Error:', error));
  });
});
