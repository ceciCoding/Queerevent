//const declarations and event listeners
const typeOfEvent = document.querySelector('.select-type');
const dateInput = document.querySelector('#date-input');
const periodicityOption = document.querySelector('.select-period');
const periodicityPreview = document.querySelector('.periodicity');
const datePreview = document.querySelector('.date');


//handling showing or not the location input
typeOfEvent.addEventListener('change', () => {
    const locationInput = document.querySelector('.location');
    const placePreview = document.querySelector('.place');

    typeOfEvent.style.color = 'black';
    if (typeOfEvent.value === 'Online') {
        locationInput.style.display = 'none';
        locationInput.querySelector('input').value = null;
        placePreview.style.display = 'none';
    } else {
        locationInput.style.display = 'flex';
        placePreview.style.display = 'block';
    }   
})

//handle showing or not periodicity
periodicityOption.addEventListener('change', () => {
    const periodicityInput = document.querySelector('.period');
    
    periodicityOption.style.color = 'black';
    if (periodicityOption.value === 'Recurring') {
        periodicityInput.style.display = 'flex';
        periodicityPreview.style.display = 'block';
        datePreview.style.display = 'none';
        dateInput.style.display = 'none';
    } else {
        periodicityInput.style.display = 'none';
        periodicityInput.querySelector('input').value = null;
        periodicityPreview.style.display = 'none';
        datePreview.style.display = 'block';
        dateInput.style.display = 'flex';
    }
})

//preview date correctly
dateInput.addEventListener('change', () => {
    const newDate = new Date(dateInput.querySelector('input').value);
    const newDateStr = newDate.toString();
    datePreview.innerHTML = newDateStr.slice(0, 16);
})

//change font color for inputs when active (placeholder can't be passed with binding logic)
document.querySelector('.form').addEventListener('click', (e) => {    
    if (e.target.type === 'text') {
          e.preventDefault();
    }
    
    if (e.target.className.includes('inpt') && e.target.style.color != 'black') {
        console.log(e.target)
         e.target.value = '';
         e.target.style.color = 'black';
    }
})