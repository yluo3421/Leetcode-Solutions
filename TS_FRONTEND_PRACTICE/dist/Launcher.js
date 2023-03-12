"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const Router_1 = require("./Router");
class Launcher {
    constructor() {
        this.router = new Router_1.Router();
    }
    launchApp() {
        console.log('App Started!');
        this.router.handleRequest();
    }
}
new Launcher().launchApp();
//# sourceMappingURL=Launcher.js.map