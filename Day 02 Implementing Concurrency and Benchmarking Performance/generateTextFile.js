const fs = require("fs");

const words = [
  "lorem", "ipsum", "dolor", "sit", "amet", "consectetur",
  "adipiscing", "elit", "integer", "nec", "odio", "praesent",
  "libero", "sed", "cursus", "ante", "dapibus", "diam",
  "sednisi", "nulla", "quis", "sem", "at", "nibh", "elementum"
];

const TARGET_WORDS = 250000;
let output = [];

for (let i = 0; i < TARGET_WORDS; i++) {
  const word = words[Math.floor(Math.random() * words.length)];
  output.push(word);
}

fs.writeFileSync("corpus.txt", output.join(" "));
console.log("corpus.txt generated with", TARGET_WORDS, "words");
