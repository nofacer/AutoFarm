import serial
import random
ser=serial.Serial('Com3',9600)
def get_temper():
    data=ser.readline()
    return data.decode()[:-2]
    # return str(random.uniform(0, 100))
    file=open("record.csv",'wb')
    file.write(data.decode()[:-2])
    file.close()