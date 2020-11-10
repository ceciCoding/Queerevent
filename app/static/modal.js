'use strict';

const overlay = document.querySelector('#overlay');
const trigger = document.querySelector('#events') || document.querySelector('main > section');
const modal = document.querySelector('#modal');
const modalLink = modal.querySelector('.link');

if (modalLink.value === '') {
    modalLink.style.display = 'none';
}

trigger.addEventListener('click', (e) => {
    if ((e.target.type === 'text' || e.target.type === 'select') && e.target.id != 'search') {
        e.preventDefault();
    }
    if (e.target.className.includes('share-arrow') || e.target.className.includes('open-m')) {
        if (modalLink.style.display != 'none') {
            modalLink.value = modalLink.value.concat(e.target.getAttribute("data-event-id"))
        }
        openModal(modal, overlay);
    }
    if (e.target.className.includes('close-button')) {
        closeModal(modal, overlay);
        if (modalLink.style.display != 'none') {
            modalLink.value = modalLink.value.slice(0, 29);
        }
    }

    //copy link text in share modal
    if (e.target.id === 'copy') {
        modalLink.select();
        modalLink.setSelectionRange(0, 99999);
        document.execCommand('copy');
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
}

function closeModal(modal, overlay) {
    if (modal === null) return;
    modal.classList.remove('active');
    overlay.classList.remove('active');
}
