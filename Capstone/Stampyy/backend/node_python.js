const { spawn } = require("child_process");
const WebSocket = require("ws");

// create websocket server
// open "client.html" in a browser and see how the images flaps between two
const wss = new WebSocket.Server({
    port: 8080
});


// feedback
wss.on('connection', ((ws) => {
    ws.on('message', (message) => {
//console.log(message.toString());
    const VideoID = message.toString();
    if (VideoID.length > 2) {
        // spawn python child process
        const py = spawn("capenv/Scripts/python.exe", ["client.py", VideoID]);

        console.log("Python child process has pid:", py.pid)

        // listen for the new image
        py.stdout.on("data", (data) => {
            console.log(data.toString())

            // broadcast the new binary image to all clients
            wss.clients.forEach((client) => {
                if (client.readyState === WebSocket.OPEN) {
                    client.send(data.toString());
                    ws.onclose = () => {
                        console.log("closed");
                        py.kill()
                    };
                }
            });

        });


        py.stderr.on("data", (data) => {
            console.error(data.toString());
        });

        }
    });
ws.send('Hello Client');
}));



