import AppError from "../utils/AppError.js";

export default function validate(schema, property = "body") {
  return (req, res, next) => {
    const dataToValidate = req[property];

    const { error, value } = schema.validate(dataToValidate, {
      abortEarly: false,
      stripUnknown: true,
    });

    if (error) {
      const message = error.details.map((d) => d.message).join(", ");
      return next(new AppError(message, "VALIDATION_ERROR", 400));
    }

    if (property === "query") {
      req.validatedQuery = value;
    } else {
      req[property] = value;
    }

    next();
  };
}
