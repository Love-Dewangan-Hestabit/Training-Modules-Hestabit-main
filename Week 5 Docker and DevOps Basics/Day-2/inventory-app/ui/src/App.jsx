import { useEffect, useState } from "react";
import ProductForm from "./components/ProductForm.jsx";
import ProductList from "./components/ProductList.jsx";

const API = "http://localhost:5000/api/products";

export default function App() {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    fetch(API)
      .then((res) => res.json())
      .then(setProducts);
  }, []);

  const addProduct = async (data) => {
    const res = await fetch(API, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data),
    });
    setProducts([...products, await res.json()]);
  };

  const updateProduct = async (id, updates) => {
    const res = await fetch(`${API}/${id}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(updates),
    });
    const updated = await res.json();
    setProducts(products.map((p) => (p._id === id ? updated : p)));
  };

  const deleteProduct = async (id) => {
    await fetch(`${API}/${id}`, { method: "DELETE" });
    setProducts(products.filter((p) => p._id !== id));
  };

  return (
    <div style={{ padding: 20 }}>
      <h2>Inventory Management</h2>
      <ProductForm onAdd={addProduct} />
      <ProductList
        products={products}
        onUpdate={updateProduct}
        onDelete={deleteProduct}
      />
    </div>
  );
}
