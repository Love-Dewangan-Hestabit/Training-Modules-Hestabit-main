import { useState } from "react";

export default function ProductForm({ onAdd }) {
  const [form, setForm] = useState({
    name: "",
    sku: "",
    quantity: "",
    price: "",
  });

  const submit = () => {
    onAdd({
      ...form,
      quantity: Number(form.quantity),
      price: Number(form.price),
    });
    setForm({ name: "", sku: "", quantity: "", price: "" });
  };

  return (
    <div>
      <input
        placeholder="Name"
        value={form.name}
        onChange={(e) => setForm({ ...form, name: e.target.value })}
      />
      <input
        placeholder="SKU"
        value={form.sku}
        onChange={(e) => setForm({ ...form, sku: e.target.value })}
      />
      <input
        placeholder="Qty"
        value={form.quantity}
        onChange={(e) => setForm({ ...form, quantity: e.target.value })}
      />
      <input
        placeholder="Price"
        value={form.price}
        onChange={(e) => setForm({ ...form, price: e.target.value })}
      />
      <button onClick={submit}>Add</button>
    </div>
  );
}
