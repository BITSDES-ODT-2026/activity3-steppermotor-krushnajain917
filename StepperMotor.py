from machine import Pin
import time

m1= Pin(13,Pin.OUT)
m2= Pin(12,Pin.OUT)
m3= Pin(14,Pin.OUT)
m4= Pin(27,Pin.OUT)

dire = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
r  = [[1,0,0,0],[0,0,0,1],[0,0,1,0],[0,1,0,0]]

while True:
    print("hii")
    for k in range(500):
        for i in dire:
            m1.value(i[0])
            m2.value(i[1])
            m3.value(i[2])
            m4.value(i[3])
            time.sleep(0.006)
    print("byee")
    for j in range(500):
        for s in r:
            m1.value(s[0])
            m2.value(s[1])
            m3.value(s[2])
            m4.value(s[3])
            time.sleep(0.006)
    print("done")
        
        

