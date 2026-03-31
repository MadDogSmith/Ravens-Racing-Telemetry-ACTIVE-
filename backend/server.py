import serial
import json
import time
from flask import Flask, render_template
from flask_socketio import SocketIO
import eventlet
eventlet.monkey_patch()

PORT = "COM4"
BAUD = 115200

# --- Serial ---
ser = serial.Serial(PORT, BAUD, timeout=1)
time.sleep(2)

# --- Web server ---
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('index.html')

def parse(line):
    data = {}
    try:
        for part in line.split(","):
            k, v = part.split("=")
            data[k] = float(v) if "." in v else int(v)
        return data
    except:
        return None

def serial_loop():
    while True:
        line = ser.readline().decode(errors="ignore").strip()
        if not line:
            continue

        data = parse(line)
        if data:
            socketio.emit("telemetry", data)

        eventlet.sleep(0.01)

if __name__ == "__main__":
    socketio.start_background_task(serial_loop)
    socketio.run(app, host="0.0.0.0", port=5000)