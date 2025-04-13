from hx711 import HX711
from config import DOUT_PIN, SCK_PIN, GAIN, CALIBRATION_WEIGHT
import time

def main():
    print("HX711 Scale Calibration")
    print("=====================")
    print("Please ensure no weight is on the scale")
    input("Press Enter when ready...")
    
    # Initialize HX711
    hx = HX711(DOUT_PIN, SCK_PIN, gain=GAIN)
    
    try:
        # Tare the scale
        print("Taring scale...")
        hx.tare()
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
            weight = hx.get_weight()
            print(f"Weight: {weight:.1f}g")
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\nCalibration cancelled by user")
    finally:
        hx.cleanup()

if __name__ == "__main__":
    main() 