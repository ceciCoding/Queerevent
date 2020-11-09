'use strict'

//both event details page and pages with events container have hearts
const container = document.querySelector('#events') || document.querySelector('.preview-info');
container.addEventListener('click', (e) => {
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



