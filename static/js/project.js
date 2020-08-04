var tl = gsap.timeline({ defaults: { opacity: 0, ease: "back" } });

function init() {
  tl.from("#demo", {
    autoAlpha: 0,
    ease: "linear",
  })
    .from("h1", {
      x: -80,
      duration: 1,
    })
    .from(
      "h2",
      {
        x: 80,
        duration: 1,
      },
      "<"
    )
    .from(
      "p",
      {
        y: 30,
      },
      "-=0.2"
    )
    .from(
      "button",
      {
        y: 50,
      },
      "-=0.4"
    )
    .from("#items > g", {
      scale: 0,
      stagger: 1,

      transformOrigin: "50% 50%",
    });
}

init();
