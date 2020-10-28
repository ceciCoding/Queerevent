'use strict';

function validateEmail() {
    const form = document.querySelector('.form');
    const email = document.querySelector('#email').value;
    const alert = document.querySelector('#alert');
    const pattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;

    if (!email.match(pattern)) {
        alert.style.display = 'block';
    } else {
        alert.style.display = 'none';
    }
}