# AcidScale

A Python project for creating a digital scale using HX711 load cell amplifier and Raspberry Pi.

## Hardware Requirements

- Raspberry Pi (any model)
- HX711 Load Cell Amplifier
- Load Cell (strain gauge)
- Jumper wires
- Power supply

## Wiring

Connect the HX711 to the Raspberry Pi as follows:
- VCC -> 3.3V
- GND -> GND
- DT (Data) -> GPIO 21 (or your chosen GPIO)
- SCK (Clock) -> GPIO 20 (or your chosen GPIO)

Connect the load cell to the HX711:
- E+ -> Load cell E+
- E- -> Load cell E-
- A+ -> Load cell A+
- A- -> Load cell A-

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
- Windows:
```bash
venv\Scripts\activate
```
- Unix/MacOS:
```bash
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Calibrate the scale:
```bash
python calibrate.py
```

2. Run the scale:
```bash
python scale.py
```

## Development

The project consists of the following components:
- `hx711.py`: Core HX711 driver implementation
- `calibrate.py`: Calibration utility
- `scale.py`: Main scale application
- `config.py`: Configuration settings

## License

MIT License 