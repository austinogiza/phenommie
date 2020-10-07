const message = document.querySelector(".messages");

const backToTop = document.querySelector(".back-to-top");

const toggle = document.querySelector(".mobile-menu");
const navLink = document.querySelector(".nav-links-container");
const navButton = document.querySelector(".nav-buttons");
const navLinks = document.querySelectorAll(".nav-links li");

const loader = document.querySelector('.pre_loader');


$(window).on('load', function () {

    setTimeout(function () {
        $('.pre_loader').fadeOut('slow');
    }, 4000)
});


window.addEventListener('load', vanish);


function vanish() {
    loader.classList.add('disappear');
}

setTimeout(function () {
    $(".messages").fadeOut("slow");
}, 3000);

window.addEventListener("scroll", scrollToTop);

function scrollToTop() {
    if (window.pageYOffset > 300) {
        backToTop.style.display = "block";
    } else {
        backToTop.style.display = "none";
    }
}

backToTop.addEventListener("click", toTop);

function toTop() {
    window.scrollTo(0, 0);
}

toggle.addEventListener("click", function menuBurger() {
    //hamburger menu
    navLink.classList.toggle("nav-links-active");

    navButton.classList.add("buttons-active");

    toggle.classList.toggle("toggle");

    //animate links
    navLinks.forEach((links, index) => {
        if (links.style.animation) {
            links.style.animation = "";
        } else {
            links.style.animation = `navLinkFade 0.8s ease-in  forwards ${index / 7 + 0.3}s`;
        }
    });
});


var scroll = new SmoothScroll('a[href*="#"]', {
    speed: 300,
    speedAsDuration: true
});

