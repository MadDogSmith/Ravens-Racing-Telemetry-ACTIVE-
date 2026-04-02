// vehicle_telemetry.ino

unsigned long lastSend = 0;
const unsigned long interval = 50; // 20Hz


void setup()
{
    Serial.begin(115200);
    delay(1000); // give time for serial to initialize
}


void loop()
{
    unsigned long now = millis();
    if (now - lastSend >= interval)
    {
        lastSend = now;

        // Smooth-ish fake telemetry
        float speed = 10 + 5 * sin(now / 1000.0);
        int rpm = 3000 + 1000 * sin(now / 700.0);
        float throttle = 0.5 + 0.5 * sin(now / 1500.0);

        Serial.print("TIME=");
        Serial.print(now);
        Serial.print(",SPEED=");
        Serial.print(speed, 2);
        Serial.print(",RPM=");
        Serial.print(rpm);
        Serial.print(",THROTTLE=");
        Serial.println(throttle, 2);
    }
}