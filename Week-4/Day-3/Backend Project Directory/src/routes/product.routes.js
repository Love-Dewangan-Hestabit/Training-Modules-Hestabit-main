import { Router } from "express";
import productController from "../controllers/product.controller.js";

const router = Router();

router.get("/products", productController.getProducts);
router.delete("/products/:id", productController.deleteProduct);

export default router;
