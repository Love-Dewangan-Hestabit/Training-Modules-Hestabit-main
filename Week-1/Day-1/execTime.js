const fs = require("fs");

function memMB() {
  return (process.memoryUsage().heapUsed / 1024 / 1024);
}

const results = {};

console.log("\n--- BUFFER (fs.readFile) ---");
let startMem = memMB();
let start = Date.now();

fs.readFile("LargeFile.txt", () => {
  const time = Date.now() - start;
  const memory = memMB() - startMem;

  console.log("Time:", time, "ms");
  console.log("Memory:", memory.toFixed(2), "MB");

  results.buffer = {
    time_ms: time,
    memory_mb: Number(memory.toFixed(2))
  };
});

setTimeout(() => {
  console.log("\n--- STREAM (fs.createReadStream) ---");
  startMem = memMB();
  start = Date.now();

  const stream = fs.createReadStream("LargeFile.txt");
  stream.on("data", () => {});

  stream.on("end", () => {
    const time = Date.now() - start;
    const memory = memMB() - startMem;

    console.log("Time:", time, "ms");
    console.log("Memory:", memory.toFixed(2), "MB");

    results.stream = {
      time_ms: time,
      memory_mb: Number(memory.toFixed(2))
    };

    
    fs.mkdirSync("logs", { recursive: true });
    fs.writeFileSync(
      "logs/day1-perf.json",
      JSON.stringify(results, null, 2)
    );

    console.log("\nResults saved to logs/day1-perf.json");
  });
}, 2000);
