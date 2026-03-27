import matplotlib.pyplot as plt
from collections import deque
import json
import sys

time_data = deque(maxlen=100)
speed_data = deque(maxlen=100)
rpm_data = deque(maxlen=100)

plt.ion()
fig, ax = plt.subplots()

while True:
    try:
        line = sys.stdin.readline()
        if not line:
            continue

        data = json.loads(line)

        time_data.append(data["TIME"])
        speed_data.append(data["SPEED"])
        rpm_data.append(data["RPM"])

        ax.clear()
        ax.plot(time_data, speed_data, label="Speed")
        ax.plot(time_data, rpm_data, label="RPM")

        ax.set_title("Live Telemetry")
        ax.legend()

        plt.pause(0.01)

    except:
        continue
