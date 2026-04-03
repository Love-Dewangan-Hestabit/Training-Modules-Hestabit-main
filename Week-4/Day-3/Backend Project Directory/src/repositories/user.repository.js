import User from "../models/User.js";

class UserRepository {
  async create(data) {
    const user = new User(data);
    return user.save();
  }

  async findById(id) {
    return User.findById(id);
  }

  async findPaginated({ limit = 10, lastId }) {
    const query = lastId ? { _id: { $lt: lastId } } : {};
    return User.find(query).sort({ _id: -1 }).limit(limit);
  }

  async update(id, data) {
    return User.findByIdAndUpdate(id, data, {
      new: true,
      runValidators: true,
    });
  }

  async delete(id) {
    return User.findByIdAndUpdate(id, { status: "INACTIVE" }, { new: true });
  }
}

export default new UserRepository();
