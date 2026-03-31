def parse_telemetry(line):
    try:
        data = {}
        parts = line.split(',')

        for part in parts:
            if '=' not in part:
                continue  # skip malformed chunks

            key, value = part.split('=', 1)

            key = key.strip()
            value = value.strip()

            # 🔥 Smart type casting
            if key in ["TIME", "RPM", "GEAR"]:
                data[key] = int(float(value))  # handles "3000.0" safely
            elif key in ["SPEED", "THROTTLE", "TEMP", "VOLTAGE"]:
                data[key] = float(value)
            else:
                # unknown fields still included (optional)
                data[key] = value

        # ✅ Only require what Arduino ACTUALLY sends
        required = ["TIME", "SPEED", "RPM", "THROTTLE"]

        if not all(k in data for k in required):
            print("[WARN] Missing required fields:", data)
            return None

        return data

    except Exception as e:
        print(f"[ERROR] Parse failed: {e} | Line: {line}")
        return None