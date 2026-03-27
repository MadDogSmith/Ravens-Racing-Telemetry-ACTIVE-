// vehicle_telemetry.ino

unsigned long lastSend = 0;
const unsigned long interval = 50; // 20Hz

void setup()
{
    Serial.begin(115200);

    // Required for Native USB boards
    while (!Serial)
    {
        ;
    }
}

void loop()
{
    while (!Serial)
        ; // Wait for serial connection
    unsigned long currentMillis = millis();
    if (currentMillis - lastMillis >= interval)
    {
        lastMillis = currentMillis;

        float speed = random(0, 2000) / 100.0; // 0-20 m/s
        float rpm = random(1000, 6000);        // 1000-6000
        float throttle = random(0, 1000) / 1000.0;
        float battery = random(0, 1000) / 1000.0; // 0-1
    }
}