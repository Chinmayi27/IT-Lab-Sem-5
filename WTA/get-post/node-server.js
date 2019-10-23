var http = require('http');
var fs = require('fs');

var server = http.createServer(function (req, res) {

    if (req.method === "GET") {
        console.log("GET call");
        res.writeHead(200, { "Content-Type": "text/html" });
        fs.createReadStream("index.html", "UTF-8").pipe(res);
    } 

    else if (req.method === "POST") {
        console.log("POST call"); 

        var body = "";
        req.on("data", function (chunk) {
            body += chunk;
        });

        req.on("end", function(){
            res.writeHead(200, { "Content-Type": "text/html" });
            res.end(body);
        });
    }

}).listen(3300);