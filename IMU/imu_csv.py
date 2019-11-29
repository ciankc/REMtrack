import serial
import time
import datetime

ser2 = serial.Serial(port='/dev/tty.usbserial-DA00VVCQ', baudrate=38400)

print("connected to: " + ser2.portstr)

while True:
    line2 = str(ser2.readline())
    val2 = line2[2:-5]
    #timestamp = str(time.time())
    timestamp = str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
    with open('imu_28_test.csv', 'a') as pyfile:
        pyfile.write(timestamp + ',' + val2 + '\n')
        
ser2.close()