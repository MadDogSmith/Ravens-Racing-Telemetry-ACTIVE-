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
                return
            except:
                print("[WARN] Waiting for serial connection...")
                time.sleep(2)

    def read_line(self):
        try:
            if self.ser and self.ser.in_waiting:
                return self.ser.readline().decode("utf-8").strip()
        except:
            print("[ERROR] Serial read failed")
            self.connect()
        return None