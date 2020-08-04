// gsap.to('.fred', {
//     xPercent: 100,
//     repeat: -1,
//     yoyo: true,
//     stagger: 0.1
// })

animation = gsap.timeline()

animation.from('.title', {
    duration: 2,
    opacity: 0,
    scale: 0,
    ease: "back"
}).from(".fred", {
    y: 100,
    stagger: 0.5,
    ease: 'back',
    duration: 0.6
}, "<")