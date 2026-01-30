import helmet from "helmet";
import cors from "cors";
import rateLimit from "express-rate-limit";
import mongoSanitize from "express-mongo-sanitize";

export function securityMiddleware(app) {
  app.use(helmet());

  app.use(
    cors({
      origin: "*",
      methods: ["GET", "POST", "PUT", "DELETE"],
    }),
  );

  app.use(
    rateLimit({
      windowMs: 15 * 60 * 1000,
      max: 100,
      message: "Too many requests, please try again later.",
    }),
  );

  app.use(
    mongoSanitize({
      replaceWith: "_",
    }),
  );
}
