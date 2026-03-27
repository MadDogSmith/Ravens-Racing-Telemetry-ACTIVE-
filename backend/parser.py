def parse_telemetry(line):
    try:
        data = {}
        parts = line.split(',')

        for part in parts:
            key, value = part.split('=')

            if key in ["TIME", "RPM", "GEAR"]:
                data[key] = int(value)
            elif key in ["SPEED", "THROTTLE", "TEMP", "VOLTAGE"]:
                data[key] = float(value)

        required = ["TIME", "SPEED", "RPM", "THROTTLE", "TEMP", "VOLTAGE", "GEAR"]
        if not all(k in data for k in required):
            return None

        return data

    except:
        return None