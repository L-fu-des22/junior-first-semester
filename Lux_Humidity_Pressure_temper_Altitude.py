'''
-*- coding:utf-8 -*-
-*- author:Lin -*-
-*- date:2019-08-29 -*-
'''

import binascii
import serial
import time
def hexShow(argv):        #十六进制显示 方法1
    try:
        result = ''
        hLen = len(argv)
        for i in range(hLen):
         hvol = argv[i]
         hhex = '%02x'%hvol
         result += hhex+' '
        print('hexShow:',result)
    except:
        pass

# 算温度
def temperature(data_other):
    temper = data_other[8:12]

    temper1="0x"+ temper[0:2]
    temper1 = int(temper1, 16)

    temper2="0x"+ temper[2:4]
    temper2 = int(temper2, 16)

    T=(temper1 << 8) | temper2
    return T/100

#算亮度
def lux(data_lux):
    lux = data_lux[8:16]

    lux1="0x"+ lux[0:2]
    lux1 = int(lux1, 16)

    lux2="0x"+ lux[2:4]
    lux2 = int(lux2, 16)

    lux3="0x"+ lux[4:6]
    lux3 = int(lux3, 16)

    lux4="0x"+ lux[6:8]
    lux4 = int(lux4, 16)

    L = (lux1 << 24) | (lux2 <<16) | (lux3 <<8)| lux4
    return L/100

# 算压力
def pressure(data_other):
    press = data_other[12:20]

    press1="0x"+ press[0:2]
    press1 = int(press1, 16)

    press2="0x"+ press[2:4]
    press2 = int(press2, 16)

    press3="0x"+ press[4:6]
    press3 = int(press3, 16)

    press4="0x"+ press[6:8]
    press4 = int(press4, 16)

    P=(press1 << 24) | (press2 << 16) | (press3 << 8) | press4
    return P/100

# 算湿度
def humidity(data_other):
    hum = data_other[20:24]

    hum1="0x"+ hum[0:2]
    hum1 = int(hum1, 16)

    hum2="0x"+ hum[2:4]
    hum2 = int(hum2, 16)

    Humi=(hum1 << 8) | hum2
    return Humi/100

# 算海拔
def altitude(data_other):
    alti = data_other[24:28]

    alti1="0x"+ alti[0:2]
    alti1 = int(alti1, 16)

    alti2="0x"+ alti[2:4]
    alti2 = int(alti2, 16)

    altitu=(alti1 << 8) | alti2
    return altitu

def data_Lux():
    
    while True:  #循环重新启动串口
        t = serial.Serial("/dev/ttyUSB0",9600)
        print(t.portstr)

        time.sleep(1)     #sleep() 与 inWaiting() 最好配对使用
        num=t.inWaiting()

        data= str(binascii.b2a_hex(t.read(num)))[2:-1] #十六进制显示方法2
    # 有时会读不出东西，但能读的时候一定是正确的数据，当有数据读出来时，执行下面if语句
        if len(data)>5:
            data_lux = data[:18]
            data_other = data[18:]
            print(data_lux)
            print(data_other)


            Lux = lux(data_lux)
            T = temperature(data_other)
            P = pressure(data_other)
            Humi = humidity(data_other)
            A = altitude(data_other)

            print('Lux:'+str(Lux)+' ,Temperature:'+str(T)+', Pressure:'+ str(P)+', \n Humidity:'+str(Humi)+', Altitude:'+str(A))
        serial.Serial.close(t)
