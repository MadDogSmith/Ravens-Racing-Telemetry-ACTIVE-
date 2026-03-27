import math
import time

class MockTelemetry:
    def __init__(self):
        self.start_time = time.time()

    def generate(self):
        t = time.time() - self.start_time

        speed = 10 + 5 * math.sin(t)              # smooth oscillation
        rpm = 3000 + 1000 * math.sin(t * 1.5)
        throttle = 0.5 + 0.5 * math.sin(t * 0.5)

        return {
            "TIME": int(t * 1000),
            "SPEED": round(speed, 2),
            "RPM": int(rpm),
            "THROTTLE": round(throttle, 2)
        }