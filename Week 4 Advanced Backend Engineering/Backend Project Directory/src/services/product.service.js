import productRepository from "../repositories/product.repository.js";
import AppError from "../utils/AppError.js";

class ProductService {
  async getProducts(query) {
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

    return productRepository.findMany({
      filter,
      sort: sortObj,
      limit: Number(limit),
    });
  }

  async deleteProduct(id) {
    const product = await productRepository.findById(id);

    if (!product) {
      throw new AppError("Product not found", "PRODUCT_NOT_FOUND", 404);
    }

    return productRepository.softDelete(id);
  }
}

export default new ProductService();
