    const openModalButtons = document.querySelectorAll('[data-modal-target]');
    const closeModalButtons = document.querySelectorAll('[close-modal-button]');
    const overlay = document.querySelector('#overlay');
    const events = document.querySelector('#events')

    events.addEventListener('click', (e) => {
        if (e.target.className === 'share-arrow') {
            const modal = document.querySelector(e.target.dataset.modalTarget);
            openModal(modal, overlay);
            console.log("targeted")
        }

        if (e.target.dataset.closeButton) {
            const modal = e.target.closest('modal');
            closeModal(modal);
        }
    });

    function openModal(modal, overlay) {
        if (modal === null) return;
        modal.classList.add('active');
        overlay.classList.add('active');
    }

    function closeModal(modal, overlay) {
        if (modal === null) return;
        modal.classList.remove('active');
        modal.classList.remove('active');
    }