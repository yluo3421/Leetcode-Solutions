import { Server } from "./Server";

class Launcher {
    private server: Server = new Server()

    public launchApp(){
        this.server.startServer();
    }

}

new Launcher().launchApp();