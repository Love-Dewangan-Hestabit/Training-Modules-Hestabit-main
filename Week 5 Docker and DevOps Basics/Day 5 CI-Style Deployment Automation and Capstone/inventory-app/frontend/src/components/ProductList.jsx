import { useState } from "react";

export default function ProductList({ products, onUpdate, onDelete }) {
  const [editingId, setEditingId] = useState(null);
  const [form, setForm] = useState({
    name: "",
    sku: "",
    quantity: "",
    price: "",
  });

  const startEdit = (product) => {
    setEditingId(product._id);
    setForm(product);
  };

  const saveEdit = () => {
    onUpdate(editingId, {
      ...form,
      quantity: Number(form.quantity),
      price: Number(form.price),
    });
    setEditingId(null);
  };

  return (
    <div className="card">
      <h3>Products</h3>

      {products.map((p) => (
        <div className="product" key={p._id}>
          {editingId === p._id ? (
            <div className="edit-row">
              <input
                value={form.name}
                onChange={(e) => setForm({ ...form, name: e.target.value })}
              />
              <input
                value={form.sku}
                onChange={(e) => setForm({ ...form, sku: e.target.value })}
              />
              <input
                type="number"
                value={form.quantity}
                onChange={(e) => setForm({ ...form, quantity: e.target.value })}
              />
              <input
                type="number"
                value={form.price}
                onChange={(e) => setForm({ ...form, price: e.target.value })}
              />

              <button onClick={saveEdit}>Save</button>
              <button onClick={() => setEditingId(null)}>Cancel</button>
            </div>
          ) : (
            <>
              <div>
                <b>{p.name}</b> ({p.sku})
                <p
                  style={{
                    color: p.quantity < 5 ? "#dc2626" : "#16a34a",
                    fontWeight: "bold",
                  }}
                >
                  Qty: {p.quantity}
                  {p.quantity < 5 && <span className="badge">LOW STOCK</span>}
                </p>
                <p>₹{p.price}</p>
              </div>

              <div>
                <button onClick={() => startEdit(p)}>Edit</button>
                <button
                  onClick={() => {
                    if (
                      confirm("Are you sure you want to delete this product?")
                    ) {
                      onDelete(p._id);
                    }
                  }}
                >
                  Delete
                </button>
              </div>
            </>
          )}
        </div>
      ))}
    </div>
  );
}
