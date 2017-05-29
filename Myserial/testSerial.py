import serial
import sys
import time

def test():
    ser = serial.Serial('/dev/ttyUSB0')
    print(ser.isOpen())
    words = "gggggg"

    while(1):
        print("send 256x\""+words+"\"to remote")
        startTime = time.time()
        times = 256
        while(times):
            times -= 1
            s = ser.write(words)

        endTime = time.time()
        print("use time:" + str(endTime-startTime))
        time.sleep(5)
    
    ser.close()


if __name__=="__main__":
    test()


