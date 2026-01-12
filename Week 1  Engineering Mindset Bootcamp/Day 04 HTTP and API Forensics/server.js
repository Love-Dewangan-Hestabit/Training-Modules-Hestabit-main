const http = require("http");
const url = require("url");

const server = http.createServer((req, res) => {
  const parsedUrl = url.parse(req.url, true);

  
  if (parsedUrl.pathname === "/echo") {
    res.writeHead(200, { "Content-Type": "application/json" });
    return res.end(JSON.stringify(req.headers, null, 2));
  }

  
  if (parsedUrl.pathname === "/slow") {
    const delay = Number(parsedUrl.query.ms) || 1000;
    return setTimeout(() => {
      res.writeHead(200);
      res.end(`Response delayed by ${delay} ms`);
    }, delay);
  }

  
  if (parsedUrl.pathname === "/cache") {
    res.writeHead(200, {
      "Cache-Control": "public, max-age=60",
      "ETag": "abc123",
    });
    return res.end("Cached response");
  }

  res.writeHead(404);
  res.end("Not Found");
});

server.listen(3000, () => {
  console.log("Server running on http://localhost:3000");
});
