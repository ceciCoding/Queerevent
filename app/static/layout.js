'use strict'
const desktopMenu = document.querySelector('.nav-container ul');
const mobileMenu = document.querySelector('.mobile-user');

desktopMenu.addEventListener('click', (e) => {
    const userImage = document.querySelector('#user-img')
    const logoutMenu = document.querySelector('.logout');
    console.log(e.target)
    if (e.target === userImage) {
        logoutMenu.classList.toggle('active');
        console.log(logoutMenu);
    }
})

//dynamic width for mobile nav
const menuContainer = document.querySelector('.mobile-nav ul');
const main = document.querySelector('main');
menuContainer.style.width = `${main.offsetWidth * 1.2}px`;
