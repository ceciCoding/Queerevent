'use strict'

//both event details page and pages with events container have hearts
const container = document.querySelector('#events') || document.querySelector('.preview-info');
container.addEventListener('click', (e) => {
    if (e.target.className.includes('heart md hydrated')) {
        console.log(e.target)
        if (e.target.className.includes('active')) {
            e.target.classList.remove('active');
            e.target.setAttribute("name", "heart-outline");
        } else {
            e.target.classList.add('active');
            e.target.setAttribute("name", "heart")
        }
    }
});