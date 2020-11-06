'use strict'
//make titles smaller 
const titles = Array.from(document.querySelectorAll('.card-text h3'));
titles.forEach(title =>  title.innerHTML = title.innerHTML.replace(/^(.{14}[^\s]*).*/, "$1"));

//display dates correctly
const dates = Array.from(document.querySelectorAll('.event-date'));
dates.forEach(date => date.innerHTML = new Date(date.innerHTML).toString().slice(0, 16));