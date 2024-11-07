import serial
import time

# Set the port and baud rate
port = '/dev/ttyUSB0'
baud_rate = 115200  # Default baud rate for Mark-10 Series 5

# Open the serial connection
ser = serial.Serial(port, baudrate=baud_rate, timeout=1)

# Command to request data
command = b'?C\r'  # Sends '?C' command to request current displayed reading

try:
    while True:
        # Send the command
        ser.write(command)

        # Allow time for the response
        time.sleep(0.1)  # Wait for 0.1 seconds between reads

        # Read the response
        response = ser.readline().decode('utf-8').strip()
        print(f"Force Gauge Reading: {response}")

except KeyboardInterrupt:
    print("\nReal-time reading stopped by user.")

except Exception as e:
    print(f"Error reading data: {e}")

finally:
    ser.close()

'''
Command Set for Data Retrieval:

- ?: Request the displayed reading.
- ?C: Request the current real-time reading.
- ?PT: Request the peak tension reading.
- ?PC: Request the peak compression reading.
- ?A: Request the average reading (if using Average Mode).
'''
