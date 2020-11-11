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

    //modal 
    if (e.target.className.includes('share-arrow') || e.target.className.includes('open-m')) {
        if (modalLink.style.display != 'none') {
            modalLink.value = modalLink.value.concat(e.target.getAttribute("data-event-id"))
        }
        openModal(modal, overlay);
    }

     //copy link text in share modal
    if (e.target.id === 'copy') {
        modalLink.select();
        modalLink.setSelectionRange(0, 99999);
        document.execCommand('copy');
    }

    if (e.target.className.includes('close-button')) {
        closeModal(modal, overlay);
        if (modalLink.style.display != 'none') {
            modalLink.value = modalLink.value.slice(0, 29);
        }
    }

    //favorites 
    if (e.target.className.includes('heart')) {
        console.log(e.target)
        if (e.target.className.includes('active')) {
            e.target.classList.remove('active');
            e.target.setAttribute("name", "heart-outline");
        } else {
            e.target.classList.add('active');
            e.target.setAttribute("name", "heart")
        }
        const eventData = {
            event: e.target.getAttribute(['data-event'])
        }

        fetch(`${window.origin}/toggle-favorite`, {
            method: 'POST',
            credentials: 'include',
            body: JSON.stringify(eventData),
            cache: "no-cache",
            headers: new Headers({
                'content-type': 'application/json'
            })
        })
            .then(response => {
                if (response.status !== 200) {
                    console.log(`Looks like there was a problem. Status Code: ${response.status}`);
                    return
                }
                response.json().then(data => {
                    console.log(data);
                });
            })
            .catch(error => {
                console.log(`Fetch error ${error}`)
            })
        
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
