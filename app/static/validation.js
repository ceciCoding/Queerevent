'use strict';
const form = document.querySelector('.form');

// function validateEmail() {
//     const email = document.querySelector('#email').value;
//     const alert = document.querySelector('#alert');
//     const pattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;

//     if (!email.match(pattern)) {
//         alert.style.display = 'block';
//     } else {
//         alert.style.display = 'none';
//     }
// }

form.addEventListener('click', (e) => {
    // e.preventDefault();
    if (e.target.type != "submit") {
        e.target.style.color = 'black';
    }
})