"use strict";
var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (Object.prototype.hasOwnProperty.call(b, p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        if (typeof b !== "function" && b !== null)
            throw new TypeError("Class extends value " + String(b) + " is not a constructor or null");
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
exports.__esModule = true;
var Comp1_1 = require("./data/components/Comp1");
var Server = /** @class */ (function () {
    function Server(port, address) {
        this.comp1 = new Comp1_1.Comp1();
        this.port = port;
        this.address = address;
    }
    Server.prototype.startServer = function () {
        console.log("Starting server at: ".concat(this.address, ": ").concat(this.port));
    };
    Server.prototype.stopServer = function () { };
    ;
    return Server;
}());
var someServer2 = new Server(8000, 'localhost');
someServer2.startServer();
var BaseServer = /** @class */ (function () {
    function BaseServer(port, address) {
        this.port = port;
        this.address = address;
    }
    BaseServer.prototype.startServer = function () {
        console.log("Starting server at: ".concat(this.address, ": ").concat(this.port));
    };
    return BaseServer;
}());
var DbServer = /** @class */ (function (_super) {
    __extends(DbServer, _super);
    function DbServer(port, address) {
        var _this = _super.call(this, port, address) || this;
        console.log('calling db server constructor');
        return _this;
    }
    DbServer.prototype.stopServer = function () {
        console.log('stopping server');
    };
    ;
    return DbServer;
}(BaseServer));
var someServer = new DbServer(8080, 'localhost');
someServer.startServer();
// however this can still access when using private
var somePort = someServer.port;
