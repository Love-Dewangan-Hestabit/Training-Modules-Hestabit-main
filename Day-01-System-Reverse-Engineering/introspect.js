const os = require("os");

function uptimeFormat(sec) {

  const d = Math.floor(sec / (3600 * 24));
  sec %= 3600 * 24;
  const hrs = Math.floor(sec / 3600);
  sec %= 3600;
  const min= Math.floor(sec / 60);
  return `${d}d ${hrs}h ${min}m`;

}

console.log(`OS: ${os.type()} ${os.release()}`);
console.log(`Architecture: ${os.arch()}`);
console.log(`CPU Cores: ${os.cpus().length}`);
console.log(`Total Memory: ${(os.totalmem() / 1024 ** 3).toFixed(2)} GB`);

console.log(`System Uptime: ${uptimeFormat(os.uptime())}`);

console.log(`Current Logged User: ${os.userInfo().username}`);

console.log(`Node Path: ${process.execPath}`);
