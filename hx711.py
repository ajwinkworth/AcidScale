import RPi.GPIO as GPIO
import time

class HX711:
    def __init__(self, dout, pd_sck, gain=128):
        """
        Initialize HX711 with the specified pins and gain.
        
        Args:
            dout (int): GPIO pin number for data output
            pd_sck (int): GPIO pin number for power down and serial clock input
            gain (int): Channel and gain factor (128, 64, or 32)
        """
        self.dout = dout
        self.pd_sck = pd_sck
        self.gain = gain
        
        # Set up GPIO
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.dout, GPIO.IN)
        GPIO.setup(self.pd_sck, GPIO.OUT)
        
        # Set initial state
        GPIO.output(self.pd_sck, False)
        
        # Calibration values
        self.offset = 0
        self.scale = 1.0
        
    def read(self):
        """
        Read raw value from HX711.
        
        Returns:
            int: Raw reading from the HX711
        """
        # Wait for the chip to be ready
        while GPIO.input(self.dout) == 1:
            time.sleep(0.001)
            
        # Read 24 bits
        value = 0
        for _ in range(24):
            GPIO.output(self.pd_sck, True)
            time.sleep(0.0001)
            value = (value << 1) | GPIO.input(self.dout)
            GPIO.output(self.pd_sck, False)
            time.sleep(0.0001)
            
        # Set channel and gain for next reading
        for _ in range(self.gain):
            GPIO.output(self.pd_sck, True)
            time.sleep(0.0001)
            GPIO.output(self.pd_sck, False)
            time.sleep(0.0001)
            
        # Convert to signed integer
        if value & 0x800000:
            value -= 0x1000000
            
        return value
    
    def get_weight(self, samples=3):
        """
        Get weight reading in grams.
        
        Args:
            samples (int): Number of samples to average
            
        Returns:
            float: Weight in grams
        """
        values = []
        for _ in range(samples):
            values.append(self.read())
            time.sleep(0.1)
            
        value = sum(values) / len(values)
        return (value - self.offset) * self.scale
    
    def tare(self, samples=10):
        """
        Tare the scale.
        
        Args:
            samples (int): Number of samples to average for tare
        """
        values = []
        for _ in range(samples):
            values.append(self.read())
            time.sleep(0.1)
            
        self.offset = sum(values) / len(values)
        
    def set_scale(self, scale):
        """
        Set the scale factor.
        
        Args:
            scale (float): Scale factor (grams per raw unit)
        """
        self.scale = scale
        
    def calibrate(self, known_weight):
        """
        Calibrate the scale with a known weight.
        
        Args:
            known_weight (float): Known weight in grams
        """
        self.tare()
        raw_value = self.read()
        self.scale = known_weight / raw_value
        
    def cleanup(self):
        """Clean up GPIO resources."""
        GPIO.cleanup() 