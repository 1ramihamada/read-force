# Force Gauge Data Streaming

This repository contains a Python script that interfaces with a Mark-10 Series 5 force gauge, reading real-time force data via a serial USB connection and outputting it continuously in the terminal. This setup is useful for applications where real-time monitoring of force readings is needed, such as load testing, quality control, and other experimental setups.

## How It Works

- The script establishes a serial connection to the force gauge over USB.
- A command is sent to request the current force reading displayed on the gauge.
- The response from the gauge is decoded and printed to the terminal in real time, providing a continuous stream of force data.

## Mark-10 Force Gauge Settings
- **Data Format**: Set to **Numeric Only** to ensure clean data output.
- **Serial/USB Settings**: Set to **USB Selected** to enable proper communication with the script.
- **Units**: Set the units to **Newtons (N)** or the desired unit for consistent output in the terminal.

## Usage Instructions
- **Connect** the force gauge to the computer via USB.
- Ensure the port variable is set to the correct serial port used by the gauge `(e.g., /dev/ttyUSB0 on Linux)`.
- Verify the `baud_rate` setting matches the gauge’s configuration (default is 115200 for Mark-10 Series 5).

## Command Set for Data Retrieval
- `?`: Request the displayed reading.
- `?C`: Request the current real-time reading.
- `?PT`: Request the peak tension reading.
- `?PC`: Request the peak compression reading.
- `?A`: Request the average reading (if using Average Mode).

## Requirements

### Hardware
- **Mark-10 Series 5 Force Gauge** (or similar model with serial/USB communication capabilities).
- **Computer with USB port** to connect to the force gauge.

### Python Libraries
- `pyserial`: for serial communication with the force gauge.

Install the required library with:
```bash
pip install pyserial
