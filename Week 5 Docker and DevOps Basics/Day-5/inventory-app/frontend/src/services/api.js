const API_URL = "/api/products";

export const getProducts = () => fetch(API_URL).then((res) => res.json());

export const addProduct = (data) =>
  fetch(API_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  }).then((res) => res.json());

export const updateProduct = (id, data) =>
  fetch(`${API_URL}/${id}`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  }).then((res) => res.json());

export const deleteProduct = (id) =>
  fetch(`${API_URL}/${id}`, { method: "DELETE" });
