"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.Router = void 0;
class Router {
    handleRequest() {
        const location = this.getRoute();
    }
    getRoute() {
        return window.location.pathname;
    }
}
exports.Router = Router;
//# sourceMappingURL=Router.js.map