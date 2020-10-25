const overlay = document.querySelector('#overlay');
const events = document.querySelector('#events');
const modal = document.querySelector('#modal')

events.addEventListener('click', (e) => {
    console.log(e.target);
    e.preventDefault();
    if (e.target.className === 'share-arrow md hydrated') {
        openModal(modal, overlay);
    }

    if (e.target.className === 'close-btn close-button' || e.target.className === 'btn close-button') {
        closeModal(modal, overlay);
    }
 });

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