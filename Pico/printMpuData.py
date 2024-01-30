import time
import adafruit_mpu6050 # type: ignore  
import busio # type: ignore
import board # type: ignore
import digitalio # type: ignore



sda_pin = board.GP16
scl_pin = board.GP17

i2c = busio.I2C(scl_pin, sda_pin)   

mpu = adafruit_mpu6050.MPU6050(i2c)

while True:
    curTime = time.monotonic() # type: ignore
    
    acc = mpu.acceleration
    added = [round(x,3) for x in acc ] 
    
    
    # 0.768448, 0.181718, -1.70216
    
    roundValue = 2
    pString = f" {curTime}, {added[0] -0.768448}, {added[1]-0.182517}, {added[2] +1.70052}, "
    print(pString)
        