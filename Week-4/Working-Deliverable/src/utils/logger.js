import winston from "winston";

const logFormat = winston.format.printf(
  ({ timestamp, level, message, requestId }) =>
    `[${timestamp}] ${level.toUpperCase()} ${
      requestId ? `[${requestId}] ` : ""
    }${message}`,
);

const logger = winston.createLogger({
  level: "info",
  format: winston.format.combine(winston.format.timestamp(), logFormat),
  transports: [
    new winston.transports.Console(),
    new winston.transports.File({ filename: "src/logs/app.log" }),
  ],
});

export default logger;
