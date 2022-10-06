import os
import time
from math import cos,sin,pi,floor 
from adafruit_rplidar import RPLidar


PORT_NAME = '/dev/ttyUSB0'
lidar = RPLidar(None,PORT_NAME)



#define variables

data = [0]*360
#displays health of the lidar
print(lidar.health)
time.sleep(5)

#will try to print out the angle value, quality, and distance 
try:
    for scan in lidar.iter_scans():
        for (quality,angle,distance) in scan:
            data[min(359,floor(angle))] = distance
            print("Angle: " + angle)
            print(quality +" " data[min(359,floor(angle))] + "\n")
except KeyboardInterrupt:
    print("Stopped")
lidar.stop()
lidar.disconnect()
