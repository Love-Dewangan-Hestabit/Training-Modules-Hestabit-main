import { Router } from "express";
import productController from "../controllers/product.controller.js";
import validate from "../middlewares/validate.js";
import { productQuerySchema } from "../validations/product.validation.js";

const router = Router();

router.get(
  "/products",
  validate(productQuerySchema, "query"),
  productController.getProducts,
);

router.post("/products/notify", productController.notifyProduct);

router.delete("/products/:id", productController.deleteProduct);

export default router;
