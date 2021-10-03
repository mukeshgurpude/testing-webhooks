import http from 'http'
import { exec } from 'child_process'

const server = http.createServer((req, res) => {
    switch (req.url) {
        case '/':
            res.write('Server is working')
            res.end()
            break;

        case '/__hook':
            if(req.method === 'POST') {
                if(req.headers['X-Github-Event'] === 'ping') {
                    res.write('pong')
                    res.end()
                    return
                }
                const parsedJson = JSON.parse(body);
                // Read and parse the JSON file
                const file = require('file.json');
                fs.writeFile(file, JSON.stringify(file), 'utf8');

                exec(`bash ${process.env.script}`)
                res.end("ok")
                return
            }
    
        default:
            break;
    }
    res.write(new Date().toDateString())
    res.end()
})

server.listen(3000)
