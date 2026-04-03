import express from "express";
import config from "../config/index.js";
import logger from "../utils/logger.js";
import dbLoader from "./db.js";
import errorMiddleware from "../middlewares/error.middleware.js";
import { securityMiddleware } from "../middlewares/security.js";
import tracingMiddleware from "../utils/tracing.js";

export default async function appLoader() {
  const app = express();

  app.use(tracingMiddleware);

  app.use(express.json({ limit: "10kb" }));

  securityMiddleware(app);

  logger.info("Middlewares loaded");

  await dbLoader();

  const routesModule = await import("../routes/index.js");
  app.use("/api", routesModule.default);

  app.use(errorMiddleware);

  app.listen(config.port, () => {
    logger.info(`Server started on port ${config.port}`);
  });
}
