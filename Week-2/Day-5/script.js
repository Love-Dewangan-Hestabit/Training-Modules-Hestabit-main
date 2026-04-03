const featuredFragrances = [
  {
    url: "https://cdn.dummyjson.com/product-images/fragrances/dolce-shine-eau-de/1.webp",
    name: "Gucci Bloom",
    description: "A garden of flowers",
  },
  {
    url: "https://cdn.dummyjson.com/product-images/fragrances/chanel-coco-noir-eau-de/1.webp",
    name: "Chanel Coco Noir",
    description: "Elegant and sophisticated",
  },
  {
    url: "https://cdn.dummyjson.com/product-images/fragrances/dior-j'adore/1.webp",
    name: "Dior J'adore",
    description: "Luxurious floral essence",
  },
  {
    url: "https://cdn.dummyjson.com/product-images/fragrances/gucci-bloom-eau-de/1.webp",
    name: "Gucci Bloom",
    description: "A garden of flowers",
  },
  {
    url: "https://cdn.dummyjson.com/product-images/mens-watches/rolex-datejust/thumbnail.webp",
    name: "Rolex Datejust",
    description: "A timeless classic",
  },
  {
    url: "https://cdn.dummyjson.com/product-images/mens-watches/rolex-cellini-date-black-dial/thumbnail.webp",
    name: "Rolex Cellini",
    description: "A classic timepiece",
  },
  {
    url: "https://cdn.dummyjson.com/product-images/mens-watches/rolex-cellini-moonphase/thumbnail.webp",
    name: "Rolex Cellini Moonphase",
    description: "A classic timepiece with a moonphase complication",
  },
  {
    url: "https://cdn.dummyjson.com/product-images/mens-watches/rolex-submariner-watch/thumbnail.webp",
    name: "Rolex Submariner",
    description: "A classic dive watch",
  },
];

const featuredGrid = document.getElementById("featuredGrid");

function displayFeaturedFragrances() {
  let html = "";

  for (let i = 0; i < featuredFragrances.length; i++) {
    const fragrance = featuredFragrances[i];

    html += '<div class="featured-card">';
    html += '  <div class="featured-image-wrapper">';
    html +=
      '    <img src="' +
      fragrance.url +
      '" alt="' +
      fragrance.name +
      '" class="featured-image">';
    html += "  </div>";
    html += '  <div class="featured-info">';
    html += '    <h3 class="featured-name">' + fragrance.name + "</h3>";
    html +=
      '    <p class="featured-description">' + fragrance.description + "</p>";
    html += "  </div>";
    html += "</div>";
  }

  featuredGrid.innerHTML = html;
}

displayFeaturedFragrances();
