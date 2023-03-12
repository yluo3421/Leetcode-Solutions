"use strict";
exports.__esModule = true;
exports.Server = void 0;
var http_1 = require("http");
var Server = /** @class */ (function () {
    function Server() {
    }
    Server.prototype.startServer = function () {
        (0, http_1.createServer)(function (req, res) {
            console.log("Got request from ".concat(req.headers['user-agent'], " for ").concat(req.url));
            res.write('hello from TS server!');
            res.end();
        }).listen(8000);
        console.log('Server started');
    };
    return Server;
}());
exports.Server = Server;
