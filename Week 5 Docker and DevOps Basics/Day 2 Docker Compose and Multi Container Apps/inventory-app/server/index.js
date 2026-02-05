import express from "express";
import mongoose from "mongoose";
import cors from "cors";
import Product from "./models/Product.js";

const app = express();
app.use(cors());
app.use(express.json());

mongoose
  .connect("mongodb://mongo:27017/inventory")
  .then(() => console.log("MongoDB connected"))
  .catch(console.error);

app.post("/api/products", async (req, res) => {
  const product = await Product.create(req.body);
  console.log("Product added:", product.sku);
  res.status(201).json(product);
});

app.get("/api/products", async (req, res) => {
  res.json(await Product.find());
});

app.put("/api/products/:id", async (req, res) => {
  const updated = await Product.findByIdAndUpdate(req.params.id, req.body, {
    new: true,
  });
  res.json(updated);
});

app.delete("/api/products/:id", async (req, res) => {
  await Product.findByIdAndDelete(req.params.id);
  res.sendStatus(204);
});

app.listen(5000, () => {
  console.log("Server running on port 5000");
});
