let count = 0;

const countDisplay = document.getElementById("count");
const increaseBtn = document.getElementById("increase");
const decreaseBtn = document.getElementById("decrease");
const addToCartBtn = document.getElementById("addToCart");

function updateCount() {
  countDisplay.textContent = count;
}

increaseBtn.addEventListener("click", function () {
  count++;
  updateCount();
});

decreaseBtn.addEventListener("click", function () {
  if (count > 0) {
    count--;
    updateCount();
  }
});

addToCartBtn.addEventListener("click", function () {
  if (count === 0) {
    alert("Please select at least 1 item.");
  } else {
    alert(`${count} item(s) added to your order.`);
    count = 0;
    updateCount();
  }
});

document.addEventListener("keydown", function (event) {
  if (event.key === "+") {
    count++;
  } else if (event.key === "-") {
    if (count > 0) count--;
  } else if (event.key === "r" || event.key === "R") {
    count = 0;
  }

  updateCount();
});
