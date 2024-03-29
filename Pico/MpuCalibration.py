import time
import adafruit_mpu6050 # type: ignore  
import busio # type: ignore
import board # type: ignore
import digitalio # type: ignore
from adafruit_lsm6ds.lsm6dsox import LSM6DSOX


sda_pin = board.GP16
scl_pin = board.GP17

i2c = busio.I2C(scl_pin, sda_pin)   

mpu = LSM6DSOX(i2c)

startTime = time.monotonic() # type: ignore
cTime = 10

finalValue = [0,0,0]
iterations = 0


print("Calibrating...")

while time.monotonic() - startTime    < cTime :
    
    currentValues = mpu.acceleration
    iterations += 1 
    
    for i in range(3):
        finalValue[i] += float(currentValues[i])
        

finalValue = [x/iterations for x in finalValue]
finalValue[2] -= 9.81
print(finalValue)
