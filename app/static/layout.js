'use strict'
const menu = document.querySelector('.nav-container ul') || document.querySelector('.mobile-user')

menu.addEventListener('click', (e) => {
    const userImage = document.querySelector('#user-img')
    const logoutMenu = document.querySelector('.logout');
    console.log(e.target)
    if (e.target === userImage) {
        logoutMenu.classList.toggle('active');
        console.log(logoutMenu);
    }
})
