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
    <div className="card">
      <h3>Add Product</h3>
      {Object.keys(form).map((key) => (
        <input
          key={key}
          placeholder={key.toUpperCase()}
          value={form[key]}
          onChange={(e) => setForm({ ...form, [key]: e.target.value })}
        />
      ))}
      <button onClick={submit}>Add</button>
    </div>
  );
}
