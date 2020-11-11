'use strict'
//make titles smaller 
const titles = Array.from(document.querySelectorAll('.card-text h3'));
titles.forEach(title =>  title.innerHTML = title.innerHTML.replace(/^(.{14}[^\s]*).*/, "$1"));

//display dates correctly
const dates = Array.from(document.querySelectorAll('.event-date'));
dates.forEach(date => date.innerHTML = new Date(date.innerHTML).toString().slice(0, 16));

//underline menu-items links
const eventsMenu = document.querySelector('.events-menu');

eventsMenu.addEventListener('click', (e) => {
    const eventFilters = document.querySelectorAll('.events-menu-item');
    const events = document.querySelectorAll('.event-container');

    eventFilters.forEach(filter => filter.classList.remove('active'))
    e.target.classList.add('active');

    events.forEach(event => {
        if (e.target.innerHTML === 'All') {
            event.style.display = 'list-item';
        }
        else if (event.getAttribute(['data-recurrence']) === e.target.innerHTML || event.getAttribute(['data-event-type']) === e.target.innerHTML) {
            event.style.display = 'list-item';
        } else {
            event.style.display = 'none';
        }
    })
})
