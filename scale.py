from hx711 import HX711
from config import DOUT_PIN, SCK_PIN, GAIN, SAMPLES
import time

def main():
    print("HX711 Scale")
    print("===========")
    
    # Initialize HX711
    hx = HX711(DOUT_PIN, SCK_PIN, gain=GAIN)
    
    # Load calibration data
    hx.load_calibration()

    try:
        print("Press Ctrl+C to exit")
        print("Reading weight...")
        
        while True:
            weight = hx.get_weight(samples=SAMPLES)
            print(f"\rWeight: {weight:.1f}g", end="")
            time.sleep(0.5)
            
    except KeyboardInterrupt:
        print("\nScale stopped by user")
    finally:
        hx.cleanup()

if __name__ == "__main__":
    main() 