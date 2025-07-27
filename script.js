const products = [
  {
    id: 1,
    name: "Wireless Headphones",
    price: 1499,
    image: "https://via.placeholder.com/200?text=Headphones"
  },
  {
    id: 2,
    name: "Smartwatch",
    price: 2499,
    image: "https://via.placeholder.com/200?text=Smartwatch"
  },
  {
    id: 3,
    name: "Laptop Sleeve",
    price: 799,
    image: "https://via.placeholder.com/200?text=Laptop+Sleeve"
  },
  {
    id: 4,
    name: "Bluetooth Speaker",
    price: 999,
    image: "https://via.placeholder.com/200?text=Speaker"
  }
];

let cartCount = 0;

function renderProducts() {
  const grid = document.getElementById("product-grid");

  products.forEach(product => {
    const card = document.createElement("div");
    card.className = "product-card";

    card.innerHTML = `
      <img src="${product.image}" alt="${product.name}" />
      <h3>${product.name}</h3>
      <p>₹${product.price}</p>
      <button onclick="addToCart()">Add to Cart</button>
    `;

    grid.appendChild(card);
  });
}

function addToCart() {
  cartCount++;
  document.getElementById("cart-count").textContent = cartCount;
}

renderProducts();
