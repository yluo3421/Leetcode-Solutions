import { Comp1 as someComponent } from './data/components/Comp1';
class Server {
    constructor(port, address) {
        this.comp1 = new someComponent();
        this.port = port;
        this.address = address;
    }
    startServer() {
        console.log(`Starting server at: ${this.address}: ${this.port}`);
    }
    stopServer() { }
    ;
}
const someServer2 = new Server(8000, 'localhost');
someServer2.startServer();
class BaseServer {
    constructor(port, address) {
        this.port = port;
        this.address = address;
    }
    startServer() {
        console.log(`Starting server at: ${this.address}: ${this.port}`);
    }
}
class DbServer extends BaseServer {
    constructor(port, address) {
        super(port, address);
        console.log('calling db server constructor');
    }
    stopServer() {
        console.log('stopping server');
    }
    ;
}
const someServer = new DbServer(8080, 'localhost');
someServer.startServer();
// however this can still access when using private
const somePort = someServer.port;
