const express = require("express");
const app = express();

let requestCount = 0;
let startTime = Date.now();

// Middleware to track requests
app.use((req, res, next) => {
  requestCount++;
  const elapsed = Math.floor((Date.now() - startTime) / 1000);
  const rps = Math.floor(requestCount / (elapsed || 1));
  console.log(
    `[${new Date().toLocaleTimeString()}] Requests: ${requestCount} | RPS: ${rps}`,
  );
  next();
});

app.get("/", (req, res) => {
  res.send("Server is running!");
});

app.get("/health", (req, res) => {
  res.json({
    status: "ok",
    uptime: Math.floor((Date.now() - startTime) / 1000),
    totalRequests: requestCount,
  });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`\n${"=".repeat(50)}`);
  console.log("DDoS Demo Server Started");
  console.log(`${"=".repeat(50)}`);
  console.log(`Server running on http://localhost:${PORT}`);
  console.log("Waiting for DDoS simulation...");
  console.log(`${"=".repeat(50)}\n`);
});

process.on("uncaughtException", (err) => {
  console.error("Uncaught Exception:", err);
});
