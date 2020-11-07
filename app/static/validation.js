'use strict';
const form = document.querySelector('.form');
const inptFile = document.querySelector('#img-upload')

form.addEventListener('click', (e) => {
    // e.preventDefault();
    if (e.target.type != "submit") {
        e.target.style.color = 'black';
    }
})

inptFile.addEventListener('change', () => {
    for (const file of inptFile.files) {
        if (file.size > 200000) {
            alert(`${file.name} is too big. Max is 200kb.`)
            inptFile.files === null;
        }
    }
})

