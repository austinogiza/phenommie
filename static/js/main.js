const message = document.querySelector('.messages');

const backToTop = document.querySelector('.back-to-top');

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