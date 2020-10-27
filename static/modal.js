'use strict';

const overlay = document.querySelector('#overlay');
const trigger = document.querySelector('#events') || document.querySelector('.open-m');
const modal = document.querySelector('#modal');
const modalLink = modal.querySelector('p');

if (modalLink.innerHTML === '') {
    modalLink.style.display = 'none';
} else {
    modalLink.classList.add('modal-link')
}

trigger.addEventListener('click', (e) => {
    console.log(e.target);
    e.preventDefault();
    if (e.target.className.includes('share-arrow') || e.target.className.includes('open-m')) {
        openModal(modal, overlay);
    }
    if (e.target.className.includes('close-button')) {
        closeModal(modal, overlay);
    }
});
 
overlay.addEventListener('click', () => {
    const modal = document.querySelector('.modal.active');
    closeModal(modal, overlay);
})

function openModal(modal, overlay) {
    if (modal === null) return;
    modal.classList.add('active');
    overlay.classList.add('active');
    console.log("function");
}

function closeModal(modal, overlay) {
    if (modal === null) return;
    modal.classList.remove('active');
    overlay.classList.remove('active');
}