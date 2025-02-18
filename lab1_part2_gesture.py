import board
import busio
import adafruit_apds9960.apds9960

i2c = board.STEMMA_I2C()

sensor=adafruit_apds9960.apds9960.APDS9960(i2c)
sensor.enable_proximity = True
sensor.enable_gesture = True

while True:
    gesture = sensor.gesture()

    if gesture == 0x01:
        print("up")
    elif gesture == 0x02:
        print("down")
    elif gesture == 0x03:
        print("left")
    elif gesture == 0x04:
        print("right")
