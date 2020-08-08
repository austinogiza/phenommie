const message = document.querySelector('.messages');

const backToTop = document.querySelector('.back-to-top');

const toggle = document.querySelector('.mobile-menu');
const navLink = document.querySelector('.nav-links-container');
const navButton = document.querySelector('.nav-buttons');
setTimeout(function () {
    $(".messages").fadeOut('slow');

}, 3000);

window.addEventListener('scroll', scrollToTop);

function scrollToTop() {

    if (window.pageYOffset > 300) {
        backToTop.style.display = 'block';
    } else {
        backToTop.style.display = 'none';
    }

}


backToTop.addEventListener('click', toTop);

function toTop() {

    window.scrollTo(0, 0);

}

toggle.addEventListener('click', function menuBurger() {
    navLink.classList.toggle('nav-links-active');

    navButton.classList.toggle('nav-buttons-active');
    toggle.classList.toggle('toggle');
});

gsap.registerPlugin(TextPlugin);
gsap.to('.phen-text', {
    text: 'Phenommie',
    ease: "power1.in",
    duration: 2,
    repeat: -1,
    yoyo: true
});