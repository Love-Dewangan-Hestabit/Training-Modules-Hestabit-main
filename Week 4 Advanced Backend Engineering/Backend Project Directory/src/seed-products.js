import mongoose from "mongoose";
import config from "./config/index.js";
import Product from "./models/Product.js";

(async () => {
  await mongoose.connect(config.databaseURL);

  await Product.create([
    { name: "iPhone 15", price: 1200 },
    { name: "Samsung Galaxy S23", price: 900 },
    { name: "Google Pixel", price: 700 },
    { name: "Nokia Phone", price: 300 },
  ]);

  console.log("Products inserted");
  process.exit(0);
})();
