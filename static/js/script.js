document.addEventListener('DOMContentLoaded', (event) => {
    // Select all dropdown elements with the class 'myDropdown'
    const dropdowns = document.querySelectorAll('.select_columns');

    // Add an event listener to each dropdown menu
    dropdowns.forEach(dropdown => {
        dropdown.addEventListener('change', function() {
 
        // Get the ID of the current dropdown
        const dropdownId = this.id;

        var customInput = document.getElementById(dropdownId + '_text');
        if (this.value == 'custom') {
            customInput.style.visibility = 'visible';
        } else {
            customInput.style.visibility  = 'hidden';
        }
        });
    });
    });
