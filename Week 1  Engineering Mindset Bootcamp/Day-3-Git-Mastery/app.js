function toUpperCaseText(text) {
    return text.toUpperCase();
}

function toLowerCaseText(text) {
  return text.toLowerCase();
}

function reverseText(text) {
  return text.split("").reverse().join("");
}


function countCharacters(text) {
  return text.length;
}


console.log("Uppercase Result:", toUpperCaseText("hello"));
console.log("Upper:", toUpperCaseText("hello"));


console.log(reverseText("Laptop"));

console.log(toLowerCaseText("ORGANIZATION"));


module.exports = {
  toUpperCaseText,
  toLowerCaseText,
  reverseText,
  countCharacters
};

// temporary debug log
