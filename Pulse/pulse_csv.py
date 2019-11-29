import serial
import time
import datetime

ser = serial.Serial(port='/dev/tty.usbmodem1421', baudrate=9600)

print("connected to: " + ser.portstr)

while True:
    line = str(ser.readline())
    val = line[2:-5]
    #timestamp = str(time.time())
    timestamp = str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
    with open('pulse_28_test.csv', 'a') as pyfile:
        pyfile.write(timestamp + ',' + val + '\n')

ser.close()