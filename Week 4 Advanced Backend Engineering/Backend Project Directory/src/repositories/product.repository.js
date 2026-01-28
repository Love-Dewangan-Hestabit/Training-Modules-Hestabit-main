import Product from "../models/Product.js";

class ProductRepository {
  async create(data) {
    const product = new Product(data);
    return product.save();
  }

  async findById(id) {
    return Product.findById(id);
  }

  async findPaginated({ limit = 10, lastId }) {
    const query = lastId ? { _id: { $lt: lastId } } : {};
    return Product.find(query).sort({ _id: -1 }).limit(limit);
  }

  async update(id, data) {
    return Product.findByIdAndUpdate(id, data, {
      new: true,
      runValidators: true,
    });
  }

  async delete(id) {
    return Product.findByIdAndUpdate(id, { status: "INACTIVE" }, { new: true });
  }
}

export default new ProductRepository();
