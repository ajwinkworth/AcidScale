# GPIO Pin Configuration
DOUT_PIN = 21  # Data pin
SCK_PIN = 20   # Clock pin

# HX711 Configuration
GAIN = 1  # Use 1 for 128 gain (CH_A_GAIN_128)

# Scale Configuration
SAMPLES = 3    # Number of samples to average for weight reading
TARE_SAMPLES = 10  # Number of samples to average for tare
CALIBRATION_WEIGHT = 100.0  # Weight in grams used for calibration

HX711_TIMEOUT = 2  # Timeout in seconds for HX711 data ready 