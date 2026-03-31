import serial
import time

class SerialInterface:
    def __init__(self, port, baudrate=115200):
        self.port = port
        self.baudrate = baudrate
        self.ser = None

    def connect(self):
        while True:
            try:
                self.ser = serial.Serial(self.port, self.baudrate, timeout=1)
                print(f"[INFO] Connected to {self.port}")
                time.sleep(2)  # allow Arduino reset
                return
            except Exception as e:
                print(f"[WARN] Waiting for serial connection... ({e})")
                time.sleep(2)

    def read_line(self):
        try:
            if self.ser:
                line = self.ser.readline().decode("utf-8", errors="ignore").strip()

                if line:
                    return line

        except Exception as e:
            print(f"[ERROR] Serial read failed: {e}")
            self.connect()

        return None


# 🔥 SELF-TEST BLOCK (this is the important part)
if __name__ == "__main__":
    print("[TEST] SerialInterface standalone test starting...")

    PORT = "COM4"
    BAUD = 115200

    s = SerialInterface(PORT, BAUD)
    s.connect()

    print("[TEST] Listening for data...\n")

    while True:
        line = s.read_line()

        if line:
            print("[RAW]", line)

        time.sleep(0.05)