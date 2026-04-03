import Joi from "joi";

export const createProductSchema = Joi.object({
  name: Joi.string().trim().min(2).required(),
  price: Joi.number().positive().required(),
  status: Joi.string().valid("ACTIVE", "INACTIVE"),
});

export const productQuerySchema = Joi.object({
  search: Joi.string().allow(""),
  minPrice: Joi.number().min(0),
  maxPrice: Joi.number().min(0),
  sort: Joi.string(),
  limit: Joi.number().min(1).max(100),
  includeDeleted: Joi.boolean(),
});
