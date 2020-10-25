const overlay = document.querySelector('#overlay');
const events = document.querySelector('#events');
const modal = document.querySelector('#modal');
const modalLink = modal.querySelector('p');

if (modalLink.innerHTML === '') {
    modalLink.style.display = 'none';
} else {
    modalLink.classList.add('modal-link')
}

events.addEventListener('click', (e) => {
    console.log(e.target);
    e.preventDefault();
    if (e.target.className === 'share-arrow md hydrated') {
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