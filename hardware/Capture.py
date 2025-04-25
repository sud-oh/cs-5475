from gpiozero import Button, PWMLED
from picamera2 import Picamera2, Preview
from datetime import datetime
import time
from time import sleep
import os
from signal import pause

camera1_dir = "NoIR_Camera"
camera2_dir = "RGB_Camera"

cam_1 = Picamera2(0)
cam_2 = Picamera2(1)

cam_1_config = cam_1.create_still_configuration({"size": (3840, 2160)})
cam_2_config = cam_2.create_still_configuration({"size": (3280, 2464)})

cam_1.configure(cam_1_config)
cam_2.configure(cam_2_config)

cam_1.start()
cam_2.start()


cameras = [[cam_1, camera1_dir], [cam_2, camera2_dir]]
count = 3

delay = 0.5

led = PWMLED(12)
led.value = .25
def capture_burst():
    led.value = .0
    for i in range(count):
        for cam_dir in cameras:
            led.value = .0
            cam = cam_dir[0]
            save_dir = cam_dir[1]
            timestamp = datetime.now().strftime("%Y%,%d_%H%M%S")
            cam.capture_file(save_dir+ "/" + save_dir + str(timestamp)+ ".jpg")
            print("Captured photo")
        sleep(delay)
    print("End Burst")
    led.value = .25

button = Button(21)
button.when_pressed = capture_burst

try:
    print("Waiting for press...")
    pause()
finally:
    print("...")


