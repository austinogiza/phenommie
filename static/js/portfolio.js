const buttons = document.querySelectorAll(".selector");
const select = document.querySelectorAll(".portfolio_case");

buttons.forEach((item) => {
  item.addEventListener("click", function () {
    buttons.forEach((item) => {
      item.className = "selector";
    });
    item.className = "active-select";
  });

  //show images
  let values = item.textContent;

});