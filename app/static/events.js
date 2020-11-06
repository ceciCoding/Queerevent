'use strict'
//make titles smaller 
const titles = Array.from(document.querySelectorAll('.card-text h3'));
const slicedTitles = titles.forEach(title =>  title.innerHTML = title.innerHTML.slice(0, 20));

//display dates correctly
const dates = Array.from(document.querySelectorAll('.event-date'));
const slicedDates = dates.forEach(date => date.innerHTML = new Date(date.innerHTML.slice(0, 10)).toString().slice(0, 16));