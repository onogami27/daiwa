import serial
import time

ser = serial.Serial("COM3", 115200, timeout=0.1)
time.sleep(2)

# ser.write({chr(123).encode())
set_dt = "123"
ser.write(set_dt.encode())
# ser.write(b'123')
ser.close()
