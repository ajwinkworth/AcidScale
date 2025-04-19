import pigpio
from hx711 import HX711
from config import DOUT_PIN, SCK_PIN, GAIN
import time

def main():
    print("HX711 Raw Data Test")
    print("====================")
    
    pi = pigpio.pi()
    if not pi.connected:
        print("Failed to connect to pigpio daemon.")
        return
    
    hx = HX711(pi, clock=SCK_PIN, data=DOUT_PIN, mode=GAIN)
    try:
        print("Press Ctrl+C to exit")
        while True:
            raw = hx.read_raw_data()
            print(f"Raw: {raw}")
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("\nTest stopped by user")
    finally:
        pi.stop()

if __name__ == "__main__":
    main() 