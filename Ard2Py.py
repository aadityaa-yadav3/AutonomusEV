import serial
import time

arduino = serial.Serial(port='COM3',   baudrate=9600, timeout=.1)


def read():
    # arduino.write(bytes(x,   'utf-8'))
    # time.sleep(0.05)
    data = arduino.readline()
    return data


while True:
    value   = read()
    print(value)
