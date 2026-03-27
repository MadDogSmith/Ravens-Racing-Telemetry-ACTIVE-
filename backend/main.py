from serial_interface import SerialInterface
from parser import parse_telemetry
from telemetry_state import TelemetryState
from mock_data import MockTelemetry

import json
import time

USE_MOCK = False  

PORT = "COM12"
BAUD = 115200

telemetry = TelemetryState()

if not USE_MOCK:
    serial_conn = SerialInterface(PORT, BAUD)
    serial_conn.connect()
else:
    mock = MockTelemetry()

print("[INFO] Backend running...\n")

while True:
    if USE_MOCK:
        data = mock.generate()
    else:
        line = serial_conn.read_line()
        data = parse_telemetry(line) if line else None

    if data:
        telemetry.update(data)
        print(json.dumps(telemetry.get()))

    time.sleep(0.05)  # ~20Hz update