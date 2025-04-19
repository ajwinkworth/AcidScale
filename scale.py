import pigpio
from hx711 import HX711
from config import DOUT_PIN, SCK_PIN, GAIN, SAMPLES
import time

def main():
    print("HX711 Scale")
    print("===========")
    
    # Initialize pigpio
    pi = pigpio.pi()
    if not pi.connected:
        print("Failed to connect to pigpio daemon.")
        return

    # Initialize HX711 (papamac's version)
    hx = HX711(pi, data=DOUT_PIN, clock=SCK_PIN, mode=GAIN)

    try:
        print("Press Ctrl+C to exit")
        print("Reading weight...")
        
        while True:
            readings = []
            error_values = {2097151, 8388607, 4194303, 262143, 65535}
            for _ in range(SAMPLES):
                w = hx.read()
                if w not in error_values and not (w is None or isinstance(w, str)):
                    readings.append(w)
                time.sleep(0.05)
            if readings:
                avg_weight = sum(readings) / len(readings)
                print(f"\rWeight: {avg_weight:.1f}g", end="")
            else:
                print("\rWeight: N/A (error)", end="")
            time.sleep(0.5)
            
    except KeyboardInterrupt:
        print("\nScale stopped by user")
    finally:
        hx._gpio.stop()  # Properly stop pigpio

if __name__ == "__main__":
    main()

# Usage Example:
# Ensure pigpio daemon is running (sudo pigpiod)
# Adjust DOUT_PIN, SCK_PIN, GAIN in config.py as needed
# Run: python scale.py 