import { Router } from "express";
import productRoutes from "./product.routes.js";

const router = Router();

router.use(productRoutes);

router.get("/health", (req, res) => {
  res.json({ status: "OK" });
});

export default router;
