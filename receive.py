import serial
import random
import time
#ser=serial.Serial('Com3',9600)
ser=serial.Serial('/dev/ttyUSB0',9600)

def get_temper():
    nowtime = time.asctime(time.localtime(time.time()))
    data=ser.readline()

    # return str(random.uniform(0, 100))
    file=open("record.csv",'wb')
    file.write(nowtime+'   '+data.decode()[:-2]+'\n')
    file.close()

    return data.decode()[:-2]