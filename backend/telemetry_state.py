class TelemetryState:
    def __init__(self):
        self.data = {
            "TIME": 0,
            "SPEED": 0.0,
            "RPM": 0,
            "THROTTLE": 0.0,
            "TEMP": 0.0,
            "VOLTAGE": 0.0,
            "GEAR": 0,
        }

    def update(self, new_data):
        if new_data:
            self.data.update(new_data)

    def get(self):
        return self.data
