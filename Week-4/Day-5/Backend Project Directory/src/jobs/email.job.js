import { Queue, Worker } from "bullmq";
import IORedis from "ioredis";
import logger from "../utils/logger.js";
import config from "../config/index.js";

const connection = new IORedis(config.redisURL, {
  maxRetriesPerRequest: null,
});

export const emailQueue = new Queue("email-queue", {
  connection,
});

export const emailWorker = new Worker(
  "email-queue",
  async (job) => {
    const { to, subject } = job.data;

    logger.info(`[JOB:${job.id}] Sending email to ${to} | Subject: ${subject}`);

    await new Promise((res) => setTimeout(res, 2000));

    if (Math.random() < 0.3) {
      throw new Error("Simulated email failure");
    }

    logger.info(`[JOB:${job.id}] Email sent successfully`);
  },
  {
    connection,
    attempts: 3,
    backoff: {
      type: "exponential",
      delay: 2000,
    },
  },
);

emailWorker.on("completed", (job) => {
  logger.info(`[JOB:${job.id}] Completed`);
});

emailWorker.on("failed", (job, err) => {
  logger.error(`[JOB:${job.id}] Failed: ${err.message}`);
});
