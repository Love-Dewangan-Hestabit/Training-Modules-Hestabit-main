import mongoose from "mongoose";
import config from "./config/index.js";
import User from "./models/User.js";
import Product from "./models/Product.js";

(async () => {
  await mongoose.connect(config.databaseURL);
  console.log("DB connected");

  const user = await User.create(
    {
      firstName: "Rohan",
      lastName: "Verma",
      email: "rohan.verma@gmail.com",
      password: "Rohan@12345",
    },
    {
      firstName: "Kritika",
      lastName: "Malhotra",
      email: "kritika.malhotra@gmail.com",
      password: "Kritika@98765",
    },
  );

  console.log("User:", user);

  const product = await Product.create(
    {
      name: "MacBook Air M4",
      price: 165000,
      totalRating: 46,
      ratingCount: 9,
    },
    {
      name: "Asus ROG Phone 9",
      price: 99000,
      totalRating: 41,
      ratingCount: 8,
    },
  );

  console.log("Product:", product);

  process.exit(0);
})();
