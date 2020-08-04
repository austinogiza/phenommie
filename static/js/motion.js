let select = e => document.querySelector(e);
let selectAll = e => document.querySelectorAll(e);

let progressSlider = select("#progressSlider");
let time = select("#time");
let pause = select("#pause"); //better than document.querySelector("#pause")

let dog = select("#dogpark");
let home = select("#home");
let school = select("#school");
let candy = select("#candy");

let animation = gsap.to('#herman', {
    duration: 6,
    ease: "none",
    motionPath: {
        path: '#motionpath',
        align: '#herman'
    },
    onUpdate: animationUpdate,
    onComplete: () => pause.innerHTML = "play",
})

// animation.pause()
// animation.progress(0.5).pause();

pause.addEventListener('click', () => {

    animation.paused(!animation.paused());

    if (animation.paused()) {
        pause.innerHTML = 'Play';
    } else {
        pause.innerHTML = 'Pause';
    };

    if (animation.progress() == 1) {

        animation.restart();
        pause.innerHTML = 'restart';



    }


});

progressSlider.addEventListener('input', function () {
    animation.progress(this.value).pause();

});

progressSlider.addEventListener('change', function () {
    pause.innerHTML = 'play';

});


function animationUpdate() {
    progressSlider.value = animation.progress();

    time.innerHTML = animation.time().toFixed(2);

}

animationUpdate();

animation.pause();
gsap.to(animation, {
    progress: 0.9,
    duration: 2,
    ease: "bounce"
});
home.addEventListener('click', function () {
    animation.pause();
    gsap.to(animation, {
        progress: 0,
        duration: 1,

    });

});

dog.addEventListener('click', function () {
    animation.pause();
    gsap.to(animation, {
        progress: 0.9,
        duration: 1,

    });

});

school.addEventListener('click', function () {
    animation.pause();
    gsap.to(animation, {
        progress: 1,
        duration: 1,

    });

});

candy.addEventListener('click', function () {
    animation.pause();
    gsap.to(animation, {
        progress: 0.5,
        duration: 1,

    });

});