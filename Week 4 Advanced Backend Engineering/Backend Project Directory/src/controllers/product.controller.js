import productService from "../services/product.service.js";
import { emailQueue } from "../jobs/email.job.js";
import logger from "../utils/logger.js";

class ProductController {
  async getProducts(req, res, next) {
    try {
      logger.info("Controller: getProducts called", {
        requestId: req.requestId,
      });

      const products = await productService.getProducts(
        req.validatedQuery || req.query,
        req.requestId,
      );

      res.json({ success: true, data: products });
    } catch (err) {
      next(err);
    }
  }

  async deleteProduct(req, res, next) {
    try {
      logger.info("Controller: deleteProduct called", {
        requestId: req.requestId,
        productId: req.params.id,
      });

      const product = await productService.deleteProduct(
        req.params.id,
        req.requestId,
      );

      res.json({ success: true, data: product });
    } catch (err) {
      next(err);
    }
  }

  async notifyProduct(req, res, next) {
    try {
      const job = await emailQueue.add("send-email", {
        to: "user@example.com",
        subject: "Product Notification",
      });

      logger.info("Controller: email job queued", {
        requestId: req.requestId,
        jobId: job.id,
      });

      res.json({
        success: true,
        message: "Email notification queued",
        jobId: job.id,
      });
    } catch (err) {
      next(err);
    }
  }
}

export default new ProductController();
