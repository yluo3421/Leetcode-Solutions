import { Comp1 as someComponent } from './data/components/Comp1';
// import { Comp1 } from '@module name set in config'


// 111.Interface
interface IServer{
    startServer(): void;
    stopServer(): void;
}
class Server {
    
    public port: number
    public address: string;
    public comp1 = new someComponent();

    constructor(port: number, address: string){
        this.port = port;
        this.address = address;

    }
    startServer() {
        console.log(`Starting server at: ${this.address}: ${this.port}`)
    }

    stopServer(): void {};
}
const someServer2: IServer = new Server(8000, 'localhost');
someServer2.startServer();



abstract class BaseServer {
    // private port: number;
    protected port: number
    protected address: string; // this will make outside the class can access address

    constructor(port: number, address: string){
        this.port = port;
        this.address = address;

    }
    startServer() {
        console.log(`Starting server at: ${this.address}: ${this.port}`)
    }

    abstract stopServer(): void
}



class DbServer extends BaseServer {
    

    constructor(port: number, address: string){
        super(port, address)
        console.log('calling db server constructor')
    }
    stopServer(): void{
        console.log('stopping server')
    };
}

const someServer = new DbServer(8080, 'localhost');
someServer.startServer();
// however this can still access when using private
const somePort = (someServer as any).port;