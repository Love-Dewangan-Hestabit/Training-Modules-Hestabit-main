import productService from "../services/product.service.js";

class ProductController {
  async getProducts(req, res, next) {
    try {
      const products = await productService.getProducts(req.query);
      res.json({ success: true, data: products });
    } catch (err) {
      next(err);
    }
  }

  async deleteProduct(req, res, next) {
    try {
      const product = await productService.deleteProduct(req.params.id);
      res.json({ success: true, data: product });
    } catch (err) {
      next(err);
    }
  }
}

export default new ProductController();
