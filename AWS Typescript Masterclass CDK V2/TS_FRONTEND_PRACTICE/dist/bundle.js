/******/ (() => { // webpackBootstrap
/******/ 	"use strict";
/******/ 	var __webpack_modules__ = ({

/***/ "./src/Router.ts":
/*!***********************!*\
  !*** ./src/Router.ts ***!
  \***********************/
/***/ ((__unused_webpack_module, exports, __webpack_require__) => {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.Router = void 0;
const Home_1 = __webpack_require__(/*! ./components/Home */ "./src/components/Home.ts");
const Login_1 = __webpack_require__(/*! ./components/Login */ "./src/components/Login.ts");
class Router {
    constructor() {
        this.mainElement = document.getElementById('main-container');
    }
    handleRequest() {
        var _a, _b;
        const location = this.getRoute();
        console.log(`Handling request for : ${location}`);
        switch (location) {
            case './login':
                (_a = this.mainElement) === null || _a === void 0 ? void 0 : _a.append(new Login_1.Login().render());
                break;
            default:
                (_b = this.mainElement) === null || _b === void 0 ? void 0 : _b.append(new Home_1.Home().render());
                break;
        }
    }
    getRoute() {
        return window.location.pathname;
    }
}
exports.Router = Router;


/***/ }),

/***/ "./src/components/Home.ts":
/*!********************************!*\
  !*** ./src/components/Home.ts ***!
  \********************************/
/***/ ((__unused_webpack_module, exports) => {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.Home = void 0;
class Home {
    constructor() {
        this.container = document.createElement('div');
    }
    render() {
        const pageLabel = document.createElement('label');
        pageLabel.innerText = 'Welcome to the Home Page!';
        this.container.append(pageLabel);
        return this.container;
    }
}
exports.Home = Home;


/***/ }),

/***/ "./src/components/Login.ts":
/*!*********************************!*\
  !*** ./src/components/Login.ts ***!
  \*********************************/
/***/ ((__unused_webpack_module, exports) => {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.Login = void 0;
class Login {
    constructor() {
        this.container = document.createElement('div');
    }
    render() {
        const pageLabel = document.createElement('label');
        pageLabel.innerText = 'Welcome to the Login Page!';
        this.container.append(pageLabel);
        return this.container;
    }
}
exports.Login = Login;


/***/ })

/******/ 	});
/************************************************************************/
/******/ 	// The module cache
/******/ 	var __webpack_module_cache__ = {};
/******/ 	
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/ 		// Check if module is in cache
/******/ 		var cachedModule = __webpack_module_cache__[moduleId];
/******/ 		if (cachedModule !== undefined) {
/******/ 			return cachedModule.exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = __webpack_module_cache__[moduleId] = {
/******/ 			// no module.id needed
/******/ 			// no module.loaded needed
/******/ 			exports: {}
/******/ 		};
/******/ 	
/******/ 		// Execute the module function
/******/ 		__webpack_modules__[moduleId](module, module.exports, __webpack_require__);
/******/ 	
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/ 	
/************************************************************************/
var __webpack_exports__ = {};
// This entry need to be wrapped in an IIFE because it need to be isolated against other modules in the chunk.
(() => {
var exports = __webpack_exports__;
/*!*************************!*\
  !*** ./src/Launcher.ts ***!
  \*************************/

Object.defineProperty(exports, "__esModule", ({ value: true }));
const Router_1 = __webpack_require__(/*! ./Router */ "./src/Router.ts");
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

})();

/******/ })()
;
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiYnVuZGxlLmpzIiwibWFwcGluZ3MiOiI7Ozs7Ozs7Ozs7Ozs7QUFBQSx3RkFBeUM7QUFDekMsMkZBQTJDO0FBRTNDLE1BQWEsTUFBTTtJQUFuQjtRQUVZLGdCQUFXLEdBQUcsUUFBUSxDQUFDLGNBQWMsQ0FBQyxnQkFBZ0IsQ0FBQztJQWtCbkUsQ0FBQztJQWhCVSxhQUFhOztRQUNoQixNQUFNLFFBQVEsR0FBRyxJQUFJLENBQUMsUUFBUSxFQUFFLENBQUM7UUFDakMsT0FBTyxDQUFDLEdBQUcsQ0FBQywwQkFBMEIsUUFBUSxFQUFFLENBQUMsQ0FBQztRQUNsRCxRQUFRLFFBQVEsRUFBRTtZQUNkLEtBQUssU0FBUztnQkFDVixVQUFJLENBQUMsV0FBVywwQ0FBRSxNQUFNLENBQUMsSUFBSSxhQUFLLEVBQUUsQ0FBQyxNQUFNLEVBQUUsQ0FBQyxDQUFDO2dCQUMvQyxNQUFNO1lBRVY7Z0JBQ0ksVUFBSSxDQUFDLFdBQVcsMENBQUUsTUFBTSxDQUFDLElBQUksV0FBSSxFQUFFLENBQUMsTUFBTSxFQUFFLENBQUMsQ0FBQztnQkFDOUMsTUFBTTtTQUNiO0lBQ0wsQ0FBQztJQUNPLFFBQVE7UUFDWixPQUFPLE1BQU0sQ0FBQyxRQUFRLENBQUMsUUFBUSxDQUFDO0lBQ3BDLENBQUM7Q0FDSjtBQXBCRCx3QkFvQkM7Ozs7Ozs7Ozs7Ozs7O0FDcEJELE1BQWEsSUFBSTtJQUFqQjtRQUNZLGNBQVMsR0FBRyxRQUFRLENBQUMsYUFBYSxDQUFDLEtBQUssQ0FBQztJQU9yRCxDQUFDO0lBTkcsTUFBTTtRQUNGLE1BQU0sU0FBUyxHQUFHLFFBQVEsQ0FBQyxhQUFhLENBQUMsT0FBTyxDQUFDLENBQUM7UUFDbEQsU0FBUyxDQUFDLFNBQVMsR0FBRywyQkFBMkIsQ0FBQztRQUNsRCxJQUFJLENBQUMsU0FBUyxDQUFDLE1BQU0sQ0FBQyxTQUFTLENBQUMsQ0FBQztRQUNqQyxPQUFPLElBQUksQ0FBQyxTQUFTO0lBQ3pCLENBQUM7Q0FDSjtBQVJELG9CQVFDOzs7Ozs7Ozs7Ozs7OztBQ1JELE1BQWEsS0FBSztJQUFsQjtRQUNZLGNBQVMsR0FBRyxRQUFRLENBQUMsYUFBYSxDQUFDLEtBQUssQ0FBQztJQU9yRCxDQUFDO0lBTkcsTUFBTTtRQUNGLE1BQU0sU0FBUyxHQUFHLFFBQVEsQ0FBQyxhQUFhLENBQUMsT0FBTyxDQUFDLENBQUM7UUFDbEQsU0FBUyxDQUFDLFNBQVMsR0FBRyw0QkFBNEIsQ0FBQztRQUNuRCxJQUFJLENBQUMsU0FBUyxDQUFDLE1BQU0sQ0FBQyxTQUFTLENBQUMsQ0FBQztRQUNqQyxPQUFPLElBQUksQ0FBQyxTQUFTO0lBQ3pCLENBQUM7Q0FDSjtBQVJELHNCQVFDOzs7Ozs7O1VDWEQ7VUFDQTs7VUFFQTtVQUNBO1VBQ0E7VUFDQTtVQUNBO1VBQ0E7VUFDQTtVQUNBO1VBQ0E7VUFDQTtVQUNBO1VBQ0E7VUFDQTs7VUFFQTtVQUNBOztVQUVBO1VBQ0E7VUFDQTs7Ozs7Ozs7Ozs7O0FDdEJBLHdFQUFrQztBQUVsQyxNQUFNLFFBQVE7SUFBZDtRQUVZLFdBQU0sR0FBVyxJQUFJLGVBQU0sRUFBRSxDQUFDO0lBTTFDLENBQUM7SUFKVSxTQUFTO1FBQ1osT0FBTyxDQUFDLEdBQUcsQ0FBQyxjQUFjLENBQUM7UUFDM0IsSUFBSSxDQUFDLE1BQU0sQ0FBQyxhQUFhLEVBQUU7SUFDL0IsQ0FBQztDQUNKO0FBRUQsSUFBSSxRQUFRLEVBQUUsQ0FBQyxTQUFTLEVBQUUsQ0FBQyIsInNvdXJjZXMiOlsid2VicGFjazovL3RzX2Zyb250ZW5kX3ByYWN0aWNlLy4vc3JjL1JvdXRlci50cyIsIndlYnBhY2s6Ly90c19mcm9udGVuZF9wcmFjdGljZS8uL3NyYy9jb21wb25lbnRzL0hvbWUudHMiLCJ3ZWJwYWNrOi8vdHNfZnJvbnRlbmRfcHJhY3RpY2UvLi9zcmMvY29tcG9uZW50cy9Mb2dpbi50cyIsIndlYnBhY2s6Ly90c19mcm9udGVuZF9wcmFjdGljZS93ZWJwYWNrL2Jvb3RzdHJhcCIsIndlYnBhY2s6Ly90c19mcm9udGVuZF9wcmFjdGljZS8uL3NyYy9MYXVuY2hlci50cyJdLCJzb3VyY2VzQ29udGVudCI6WyJpbXBvcnQgeyBIb21lIH0gZnJvbSBcIi4vY29tcG9uZW50cy9Ib21lXCI7XG5pbXBvcnQgeyBMb2dpbiB9IGZyb20gXCIuL2NvbXBvbmVudHMvTG9naW5cIjtcblxuZXhwb3J0IGNsYXNzIFJvdXRlciB7XG5cbiAgICBwcml2YXRlIG1haW5FbGVtZW50ID0gZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoJ21haW4tY29udGFpbmVyJylcblxuICAgIHB1YmxpYyBoYW5kbGVSZXF1ZXN0KCl7XG4gICAgICAgIGNvbnN0IGxvY2F0aW9uID0gdGhpcy5nZXRSb3V0ZSgpO1xuICAgICAgICBjb25zb2xlLmxvZyhgSGFuZGxpbmcgcmVxdWVzdCBmb3IgOiAke2xvY2F0aW9ufWApO1xuICAgICAgICBzd2l0Y2ggKGxvY2F0aW9uKSB7XG4gICAgICAgICAgICBjYXNlICcuL2xvZ2luJzpcbiAgICAgICAgICAgICAgICB0aGlzLm1haW5FbGVtZW50Py5hcHBlbmQobmV3IExvZ2luKCkucmVuZGVyKCkpO1xuICAgICAgICAgICAgICAgIGJyZWFrO1xuICAgICAgICBcbiAgICAgICAgICAgIGRlZmF1bHQ6XG4gICAgICAgICAgICAgICAgdGhpcy5tYWluRWxlbWVudD8uYXBwZW5kKG5ldyBIb21lKCkucmVuZGVyKCkpO1xuICAgICAgICAgICAgICAgIGJyZWFrO1xuICAgICAgICB9XG4gICAgfVxuICAgIHByaXZhdGUgZ2V0Um91dGUoKXtcbiAgICAgICAgcmV0dXJuIHdpbmRvdy5sb2NhdGlvbi5wYXRobmFtZTtcbiAgICB9XG59IiwiXG5cblxuZXhwb3J0IGNsYXNzIEhvbWUge1xuICAgIHByaXZhdGUgY29udGFpbmVyID0gZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgnZGl2JylcbiAgICByZW5kZXIoKXtcbiAgICAgICAgY29uc3QgcGFnZUxhYmVsID0gZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgnbGFiZWwnKTtcbiAgICAgICAgcGFnZUxhYmVsLmlubmVyVGV4dCA9ICdXZWxjb21lIHRvIHRoZSBIb21lIFBhZ2UhJztcbiAgICAgICAgdGhpcy5jb250YWluZXIuYXBwZW5kKHBhZ2VMYWJlbCk7XG4gICAgICAgIHJldHVybiB0aGlzLmNvbnRhaW5lclxuICAgIH1cbn0iLCJcblxuXG5leHBvcnQgY2xhc3MgTG9naW4ge1xuICAgIHByaXZhdGUgY29udGFpbmVyID0gZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgnZGl2JylcbiAgICByZW5kZXIoKXtcbiAgICAgICAgY29uc3QgcGFnZUxhYmVsID0gZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgnbGFiZWwnKTtcbiAgICAgICAgcGFnZUxhYmVsLmlubmVyVGV4dCA9ICdXZWxjb21lIHRvIHRoZSBMb2dpbiBQYWdlISc7XG4gICAgICAgIHRoaXMuY29udGFpbmVyLmFwcGVuZChwYWdlTGFiZWwpO1xuICAgICAgICByZXR1cm4gdGhpcy5jb250YWluZXJcbiAgICB9XG59IiwiLy8gVGhlIG1vZHVsZSBjYWNoZVxudmFyIF9fd2VicGFja19tb2R1bGVfY2FjaGVfXyA9IHt9O1xuXG4vLyBUaGUgcmVxdWlyZSBmdW5jdGlvblxuZnVuY3Rpb24gX193ZWJwYWNrX3JlcXVpcmVfXyhtb2R1bGVJZCkge1xuXHQvLyBDaGVjayBpZiBtb2R1bGUgaXMgaW4gY2FjaGVcblx0dmFyIGNhY2hlZE1vZHVsZSA9IF9fd2VicGFja19tb2R1bGVfY2FjaGVfX1ttb2R1bGVJZF07XG5cdGlmIChjYWNoZWRNb2R1bGUgIT09IHVuZGVmaW5lZCkge1xuXHRcdHJldHVybiBjYWNoZWRNb2R1bGUuZXhwb3J0cztcblx0fVxuXHQvLyBDcmVhdGUgYSBuZXcgbW9kdWxlIChhbmQgcHV0IGl0IGludG8gdGhlIGNhY2hlKVxuXHR2YXIgbW9kdWxlID0gX193ZWJwYWNrX21vZHVsZV9jYWNoZV9fW21vZHVsZUlkXSA9IHtcblx0XHQvLyBubyBtb2R1bGUuaWQgbmVlZGVkXG5cdFx0Ly8gbm8gbW9kdWxlLmxvYWRlZCBuZWVkZWRcblx0XHRleHBvcnRzOiB7fVxuXHR9O1xuXG5cdC8vIEV4ZWN1dGUgdGhlIG1vZHVsZSBmdW5jdGlvblxuXHRfX3dlYnBhY2tfbW9kdWxlc19fW21vZHVsZUlkXShtb2R1bGUsIG1vZHVsZS5leHBvcnRzLCBfX3dlYnBhY2tfcmVxdWlyZV9fKTtcblxuXHQvLyBSZXR1cm4gdGhlIGV4cG9ydHMgb2YgdGhlIG1vZHVsZVxuXHRyZXR1cm4gbW9kdWxlLmV4cG9ydHM7XG59XG5cbiIsImltcG9ydCB7IFJvdXRlciB9IGZyb20gXCIuL1JvdXRlclwiO1xuXG5jbGFzcyBMYXVuY2hlciB7XG5cbiAgICBwcml2YXRlIHJvdXRlcjogUm91dGVyID0gbmV3IFJvdXRlcigpO1xuXG4gICAgcHVibGljIGxhdW5jaEFwcCgpIHtcbiAgICAgICAgY29uc29sZS5sb2coJ0FwcCBTdGFydGVkIScpXG4gICAgICAgIHRoaXMucm91dGVyLmhhbmRsZVJlcXVlc3QoKVxuICAgIH1cbn1cblxubmV3IExhdW5jaGVyKCkubGF1bmNoQXBwKCk7Il0sIm5hbWVzIjpbXSwic291cmNlUm9vdCI6IiJ9