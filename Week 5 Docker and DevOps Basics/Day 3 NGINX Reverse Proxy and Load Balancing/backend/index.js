const express = require("express");
const app = express();

const PORT = 3000;

app.get("/api", (req, res) => {
  res.json({
    message: "Backend Server Working",
    container: process.env.HOSTNAME,
  });
});

app.listen(PORT, () => {
  console.log(`Backend running on port ${PORT}`);
});
