import dotenv from "dotenv";

const env = process.env.NODE_ENV || "local";

dotenv.config({
  path: `.env.${env}`,
});

export default {
  env,
  port: process.env.PORT,
  databaseURL: process.env.DATABASE_URL,
};
