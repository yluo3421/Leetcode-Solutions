"use strict";
exports.__esModule = true;
var Server_1 = require("./Server");
var Launcher = /** @class */ (function () {
    function Launcher() {
        this.server = new Server_1.Server();
    }
    Launcher.prototype.launchApp = function () {
        this.server.startServer();
    };
    return Launcher;
}());
new Launcher().launchApp();
