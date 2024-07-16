document.addEventListener('DOMContentLoaded', (event) => {
    const dropdowns = document.querySelectorAll('.select_columns');
    dropdowns.forEach(dropdown => {
        dropdown.addEventListener('change', function() {
 
       
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

    var currentURL = window.location.href;
    var ID = currentURL.match(/\w+$/);
    console.log(document);
    if (ID) {
        var link = document.getElementsByName(ID[0]);

        if (link.length > 0) {
            link[0].classList.add('active');
        } else {
            console.log('No element found with the name:', ID[0]);
        }
    } else {
        console.log('No match found in the URL');
    }