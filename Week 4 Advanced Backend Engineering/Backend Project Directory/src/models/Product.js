import mongoose from "mongoose";

const productSchema = new mongoose.Schema(
  {
    name: {
      type: String,
      required: true,
      trim: true,
      lowercase: true,
    },

    price: {
      type: Number,
      required: true,
      min: 0,
    },

    totalRating: {
      type: Number,
      default: 0,
    },

    ratingCount: {
      type: Number,
      default: 0,
    },

    status: {
      type: String,
      enum: ["ACTIVE", "INACTIVE"],
      default: "ACTIVE",
    },
  },
  {
    timestamps: true,
  },
);

productSchema.virtual("rating").get(function () {
  if (this.ratingCount === 0) return 0;
  return this.totalRating / this.ratingCount;
});

productSchema.index({ status: 1, createdAt: -1 });

const Product = mongoose.model("Product", productSchema);
export default Product;
