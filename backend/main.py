from backend.serial_utils import SerialInterface
from parser import parse_telemetry
from telemetry_state import TelemetryState
from mock_data import MockTelemetry

import json
import time

USE_MOCK = False   #TURNED OFF MOCK

PORT = "COM4"
BAUD = 115200

telemetry = TelemetryState()

if not USE_MOCK:
    print("[DEBUG] Connecting to serial...")
    serial_conn = SerialInterface(PORT, BAUD)
    serial_conn.connect()
    print("[DEBUG] Serial connected.")
    time.sleep(2)  # give Arduino time to reset
else:
    mock = MockTelemetry()

print("[INFO] Backend running...\n")

while True:
    try:
        if USE_MOCK:
            data = mock.generate()

        else:
            line = serial_conn.read_line()

            # 🔍 DEBUG RAW SERIAL
            if line:
                print("[RAW]", line)

            if not line:
                continue

            data = parse_telemetry(line)

        if data:
            telemetry.update(data)
            print("[PARSED]", json.dumps(telemetry.get(), indent=2))

    except Exception as e:
        print("[ERROR]", e)

    time.sleep(0.05)  # ~20Hz