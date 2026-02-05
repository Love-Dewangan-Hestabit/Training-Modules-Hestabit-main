import { useState } from "react";

export default function ProductList({ products, onUpdate, onDelete }) {
  const [editingId, setEditingId] = useState(null);
  const [editForm, setEditForm] = useState({
    name: "",
    sku: "",
    quantity: "",
    price: "",
  });

  const startEdit = (product) => {
    setEditingId(product._id);
    setEditForm({
      name: product.name,
      sku: product.sku,
      quantity: product.quantity,
      price: product.price,
    });
  };

  const saveEdit = (id) => {
    onUpdate(id, {
      name: editForm.name,
      sku: editForm.sku,
      quantity: Number(editForm.quantity),
      price: Number(editForm.price),
    });
    setEditingId(null);
  };

  return (
    <div>
      <h3>Products</h3>

      {products.map((p) => (
        <div key={p._id} style={{ marginBottom: 10 }}>
          {editingId === p._id ? (
            <>
              <input
                placeholder="Name"
                value={editForm.name}
                onChange={(e) =>
                  setEditForm({ ...editForm, name: e.target.value })
                }
              />
              <input
                placeholder="SKU"
                value={editForm.sku}
                onChange={(e) =>
                  setEditForm({ ...editForm, sku: e.target.value })
                }
              />
              <input
                placeholder="Qty"
                type="number"
                value={editForm.quantity}
                onChange={(e) =>
                  setEditForm({ ...editForm, quantity: e.target.value })
                }
              />
              <input
                placeholder="Price"
                type="number"
                value={editForm.price}
                onChange={(e) =>
                  setEditForm({ ...editForm, price: e.target.value })
                }
              />

              <button onClick={() => saveEdit(p._id)}>Save</button>
              <button onClick={() => setEditingId(null)}>Cancel</button>
            </>
          ) : (
            <>
              <b>{p.name}</b> ({p.sku}) - Qty: {p.quantity} - ₹{p.price}
              <button onClick={() => startEdit(p)}>Edit</button>
              <button onClick={() => onDelete(p._id)}>Delete</button>
            </>
          )}
        </div>
      ))}
    </div>
  );
}
