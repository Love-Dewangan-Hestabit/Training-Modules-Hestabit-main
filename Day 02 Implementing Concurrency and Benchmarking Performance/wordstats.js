#!/usr/bin/env node
const fs = require("fs");

const args = process.argv.slice(2);

function getArg(flag, defaultValue = null) {
  const index = args.indexOf(flag);
  return index !== -1 ? args[index + 1] : defaultValue;
}

const filePath =  getArg("--file");

const topN = Number(getArg("--top", 10));
const minLen = Number(getArg("--minLen", 1));
const concurrency = Number(getArg("--concurrency", 1));

if (!filePath) {
  console.error("Usage: node wordstat.js --file corpus.txt --top 10 --minLen 5 --concurrency 4");
  process.exit(1);
}

const text = fs.readFileSync(filePath, "utf-8");

const chunkSize = Math.ceil(text.length / concurrency);
const chunks = [];

for (let i = 0; i < concurrency; i++) {
  chunks.push(text.slice(i * chunkSize, (i + 1) * chunkSize));
}

function processChunk(chunk) {
  return new Promise((resolve) => {
    const words = chunk.toLowerCase().match(/\b[a-z]+\b/g) || [];

    const freq = {};
    let totalWords = 0;
    let longestWord = "";
    let shortestWord = null;

    for (const word of words) {
      totalWords++; 

      if (word.length < minLen) continue;

      freq[word] = (freq[word] || 0) + 1;

      if (word.length > longestWord.length) longestWord = word;
      if (!shortestWord || word.length < shortestWord.length) {
        shortestWord = word;
      }
    }

    resolve({ freq, totalWords, longestWord, shortestWord });
  });
}


async function run() {
  const startTime = Date.now();
  const startMem = process.memoryUsage().heapUsed;

  const results = await Promise.all(chunks.map(processChunk));


  const freq = {};
  let totalWords = 0;
  let longestWord = "";
  let shortestWord = null;

  for (const res of results) {
    totalWords += res.totalWords;

    if (res.longestWord.length > longestWord.length) {
      longestWord = res.longestWord;
    }

    if (!shortestWord || res.shortestWord.length < shortestWord.length) {
      shortestWord = res.shortestWord;
    }

    for (const [word, count] of Object.entries(res.freq)) {
      freq[word] = (freq[word] || 0) + count;
    }
  }

  const sorted = Object.entries(freq)
    .sort((a, b) => b[1] - a[1])
    .slice(0, topN);

  const timeMs = Date.now() - startTime;
  const memoryMB = (
    (process.memoryUsage().heapUsed - startMem) / 1024 / 1024
  ).toFixed(2);

  fs.mkdirSync("output", { recursive: true });

  const stats = {
    concurrency,
    totalWords,
    uniqueWords: Object.keys(freq).length,
    longestWord,
    shortestWord,
    topWords: sorted.map(([word, count]) => ({ word, count })),
  };

  fs.writeFileSync(
    `output/stats-${concurrency}.json`,
    JSON.stringify(stats, null, 2)
  );


  fs.mkdirSync("logs", { recursive: true });

  const perf = {
    concurrency,
    timeMs,
    memoryMB: Number(memoryMB),
  };

  fs.writeFileSync(
    `logs/perf-summary${concurrency}.json`,
    JSON.stringify(perf, null, 2)
  );

  
  console.log("\nWord Statistics");
  console.log("Total words   :", totalWords);
  console.log("Unique words  :", Object.keys(freq).length);
  console.log("Longest word  :", longestWord);
  console.log("Shortest word :", shortestWord);

  console.log(`\nTop ${topN} words`);
  sorted.forEach(([word, count], i) => {
    console.log(`${i + 1}. ${word} - ${count}`);
  });

  console.log("\nPerformance");
  console.log("Concurrency :", concurrency);
  console.log("Time (ms)   :", timeMs);
  console.log("Memory (MB) :", memoryMB);
}

run().catch(console.error);
