import productRepository from "../repositories/product.repository.js";
import AppError from "../utils/AppError.js";
import logger from "../utils/logger.js";

class ProductService {
  async getProducts(query, requestId) {
    logger.info("ProductService: building product query", {
      requestId,
    });

    const {
      search,
      minPrice,
      maxPrice,
      sort,
      includeDeleted,
      limit = 10,
    } = query;

    const filter = {};

    if (search) {
      filter.$or = [{ name: { $regex: search, $options: "i" } }];
    }

    if (minPrice || maxPrice) {
      filter.price = {};
      if (minPrice) filter.price.$gte = Number(minPrice);
      if (maxPrice) filter.price.$lte = Number(maxPrice);
    }

    if (!includeDeleted) {
      filter.deletedAt = null;
    }

    let sortObj = { createdAt: -1 };

    if (sort) {
      const [field, order] = sort.split(":");
      sortObj = { [field]: order === "desc" ? -1 : 1 };
    }

    logger.info("ProductService: fetching products from repository", {
      requestId,
      filter,
      sort: sortObj,
      limit,
    });

    return productRepository.findMany({
      filter,
      sort: sortObj,
      limit: Number(limit),
    });
  }

  async deleteProduct(id, requestId) {
    logger.info("ProductService: deleting product", {
      requestId,
      productId: id,
    });

    const product = await productRepository.findById(id);

    if (!product) {
      logger.warn("ProductService: product not found", {
        requestId,
        productId: id,
      });
      throw new AppError("Product not found", "PRODUCT_NOT_FOUND", 404);
    }

    return productRepository.softDelete(id);
  }
}

export default new ProductService();
