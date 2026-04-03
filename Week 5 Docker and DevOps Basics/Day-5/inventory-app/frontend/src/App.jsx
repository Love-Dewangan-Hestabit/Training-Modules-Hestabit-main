import { useEffect, useState } from "react";
import Navbar from "./components/Navbar";
import ProductForm from "./components/ProductForm";
import ProductList from "./components/ProductList";
import InventoryStats from "./components/InventoryStats";
import {
  getProducts,
  addProduct,
  updateProduct,
  deleteProduct,
} from "./services/api";

export default function App() {
  const [products, setProducts] = useState([]);
  const [search, setSearch] = useState("");

  useEffect(() => {
    getProducts().then(setProducts);
  }, []);

  const filteredProducts = products.filter(
    (p) =>
      p.name.toLowerCase().includes(search.toLowerCase()) ||
      p.sku.toLowerCase().includes(search.toLowerCase()),
  );

  return (
    <>
      <Navbar />
      <main className="container">
        <InventoryStats products={products} />

        <input
          className="search"
          placeholder="Search by name or SKU..."
          value={search}
          onChange={(e) => setSearch(e.target.value)}
        />

        <ProductForm
          onAdd={async (data) => {
            const product = await addProduct(data);
            setProducts([product, ...products]);
          }}
        />

        <ProductList
          products={filteredProducts}
          onUpdate={async (id, data) => {
            const updated = await updateProduct(id, data);
            setProducts(products.map((p) => (p._id === id ? updated : p)));
          }}
          onDelete={async (id) => {
            await deleteProduct(id);
            setProducts(products.filter((p) => p._id !== id));
          }}
        />
      </main>
    </>
  );
}
