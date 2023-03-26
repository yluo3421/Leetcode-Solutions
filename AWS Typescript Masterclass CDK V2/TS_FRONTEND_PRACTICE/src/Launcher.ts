import { Router } from "./Router";

class Launcher {

    private router: Router = new Router();

    public launchApp() {
        console.log('App Started!')
        this.router.handleRequest()
    }
}

new Launcher().launchApp();