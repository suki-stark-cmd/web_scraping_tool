import serial
import webbrowser

# Set your serial port (adjust as needed)
ser = serial.Serial('COM6', 115200, timeout=1)

while True:
    line = ser.readline().decode('utf-8').strip()
    if "Key Value:" in line:
        # Extract key from the serial line
        key_value = line.split(":")[1].strip()
        url = f"http://localhost:8000/myapp/nfc-scan/{key_value}/"  # Update with your Django server URL
        print(f"Navigating to {url}")
        webbrowser.open(url)  # Open the URL in the default browser