import express from "express";
import config from "../config/index.js";
import logger from "../utils/logger.js";
import dbLoader from "./db.js";

export default async function appLoader() {
  const app = express();

  app.use(express.json());
  logger.info("Middlewares loaded");

  await dbLoader();

  const routes = (await import("../routes/index.js")).default;
  app.use("/api", routes);

  const routeCount = routes.stack.filter((layer) => layer.route).length;
  logger.info(`Routes mounted: ${routeCount} endpoints`);

  app.listen(config.port, () => {
    logger.info(`Server started on port ${config.port}`);
  });
}
