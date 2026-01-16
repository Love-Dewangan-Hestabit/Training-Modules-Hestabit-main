let allProducts = [];
let filteredProducts = [];

const allowedCategories = [
  "fragrances",
  "home-decoration",
  "laptops",
  "mens-shoes",
  "mens-watches",
  "smartphones",
  "sunglasses",
  "womens-bags",
  "womens-jewellery",
  "womens-shoes",
  "womens-watches",
  "beauty",
];

const productsGrid = document.getElementById("productsGrid");
const searchInput = document.getElementById("searchInput");
const searchContainer = document.getElementById("searchContainer");
const searchToggle = document.getElementById("searchToggle");
const sortSelect = document.getElementById("sortSelect");
const categorySelect = document.getElementById("categorySelect");
const resultsCount = document.getElementById("resultsCount");

searchToggle.addEventListener("click", function () {
  searchContainer.classList.toggle("active");
  if (searchContainer.classList.contains("active")) {
    searchInput.focus();
  }
});

function fetchProducts() {
  fetch("https://dummyjson.com/products?limit=200")
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
      allProducts = data.products.filter(function (product) {
        return allowedCategories.includes(product.category.toLowerCase());
      });

      filteredProducts = allProducts;

      populateCategories(allProducts);
      displayProducts(filteredProducts);
      updateResultsCount(filteredProducts.length);
    })
    .catch(function () {
      productsGrid.innerHTML =
        '<div class="loading">Failed to load products. Please try again.</div>';
    });
}

function populateCategories(products) {
  const categories = [];

  for (let i = 0; i < products.length; i++) {
    if (!categories.includes(products[i].category)) {
      categories.push(products[i].category);
    }
  }

  categories.sort();

  let html = '<option value="all">All Categories</option>';

  for (let i = 0; i < categories.length; i++) {
    html += `<option value="${categories[i]}">${
      categories[i].charAt(0).toUpperCase() + categories[i].slice(1)
    }</option>`;
  }

  categorySelect.innerHTML = html;
}

function generateStars(rating) {
  const roundedRating = Math.round(rating);
  let stars = "";

  for (let i = 1; i <= 5; i++) {
    stars += i <= roundedRating ? "★" : "☆";
  }

  return stars;
}

function displayProducts(products) {
  if (products.length === 0) {
    productsGrid.innerHTML = '<div class="loading">No products found.</div>';
    return;
  }

  let html = "";

  for (let i = 0; i < products.length; i++) {
    const product = products[i];

    html += '<div class="product-card">';
    html += '  <div class="product-image-wrapper">';
    html += `    <img src="${product.thumbnail}" alt="${product.title}" class="product-image">`;
    html += "  </div>";

    html += '  <div class="product-info">';
    html += `    <div class="product-category">${product.category.toUpperCase()}</div>`;
    html += `    <h3 class="product-title">${product.title}</h3>`;
    html += `    <div class="product-price">$${product.price}</div>`;

    html += '    <div class="product-rating">';
    html += `      <span class="stars">${generateStars(product.rating)}</span>`;
    html += `      <span>(${product.rating})</span>`;
    html += "    </div>";

    html += "  </div>";
    html += "</div>";
  }

  productsGrid.innerHTML = html;
}

function updateResultsCount(count) {
  if (count === allProducts.length) {
    resultsCount.textContent = `Showing all ${count} products`;
  } else {
    resultsCount.textContent = `Showing ${count} of ${allProducts.length} products`;
  }
}

function applyFilters() {
  const searchTerm = searchInput.value.toLowerCase();
  const selectedCategory = categorySelect.value;

  filteredProducts = allProducts.filter(function (product) {
    const matchesSearch =
      product.title.toLowerCase().includes(searchTerm) ||
      product.category.toLowerCase().includes(searchTerm) ||
      product.description.toLowerCase().includes(searchTerm);

    const matchesCategory =
      selectedCategory === "all" || product.category === selectedCategory;

    return matchesSearch && matchesCategory;
  });

  updateResultsCount(filteredProducts.length);
  applyCurrentSort();
}

searchInput.addEventListener("input", function () {
  applyFilters();
});

categorySelect.addEventListener("change", function () {
  applyFilters();
});

sortSelect.addEventListener("change", function () {
  applyCurrentSort();
});

function applyCurrentSort() {
  const sortValue = sortSelect.value;
  let sortedProducts = filteredProducts.slice();

  if (sortValue === "price-high") {
    sortedProducts.sort((a, b) => b.price - a.price);
  } else if (sortValue === "price-low") {
    sortedProducts.sort((a, b) => a.price - b.price);
  } else if (sortValue === "name") {
    sortedProducts.sort((a, b) => a.title.localeCompare(b.title));
  } else if (sortValue === "rating-high") {
    sortedProducts.sort((a, b) => b.rating - a.rating);
  } else if (sortValue === "rating-low") {
    sortedProducts.sort((a, b) => a.rating - b.rating);
  }

  displayProducts(sortedProducts);
}

fetchProducts();
