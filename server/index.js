const express = require("express");
const http = require("http");
const { Server } = require("socket.io");
const cors = require("cors");

const app = express();
app.use(cors());

const server = http.createServer(app);

const io = new Server(server, {
    cors: {
        origin: "http://localhost:5173",
        methods: ["GET", "POST"]
    }
});

setInterval(() => {
    io.emit("telemetry", {
        time: Date.now(),
        speed: Math.floor(Math.random() * 120),
        rpm: Math.floor(Math.random() * 8000)
    });
    
}, 100);

server.listen(3001, () => {
    console.log("Server running on port 3001");
});