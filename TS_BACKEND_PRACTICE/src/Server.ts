import { createServer, IncomingMessage, ServerResponse } from 'http';

export class Server {
    public startServer(){
        createServer(
            (req: IncomingMessage, res: ServerResponse) => {
                console.log(`Got request from ${req.headers['user-agent']} for ${req.url}`)
                res.write('hello from TS server!')
                res.end();
            }
        ).listen(8000)
        console.log('Server started')
    }
}