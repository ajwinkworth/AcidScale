from hx711 import HX711
from config import DOUT_PIN, SCK_PIN, GAIN, CALIBRATION_WEIGHT
import time
import pigpio

def main():
    print("HX711 Scale Calibration")
    print("=====================")
    print("Please ensure no weight is on the scale")
    input("Press Enter when ready...")
    
    # Initialize pigpio and HX711
    pi = pigpio.pi()
    if not pi.connected:
        print("Failed to connect to pigpio daemon.")
        return
    hx = HX711(pi, clock=SCK_PIN, data=DOUT_PIN, mode=GAIN)
    
    try:
        # Tare the scale
        print("Taring scale...")
        hx.zero()
        print("Tare complete!")
        
        # Wait for calibration weight
        print(f"\nPlease place a {CALIBRATION_WEIGHT}g weight on the scale")
        input("Press Enter when ready...")
        
        # Calibrate
        print("Calibrating...")
        hx.calibrate(CALIBRATION_WEIGHT)
        print("Calibration complete!")
        
        # Test reading
        print("\nTesting scale...")
        for _ in range(5):
            weight = hx.read()
            print(f"Weight: {weight:.1f}g")
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\nCalibration cancelled by user")
    finally:
        pi.stop()

if __name__ == "__main__":
    main() 