import RPistepper as stp
from picamera import PiCamera
from PIL import Image 
import time
import os

M1_pins = [17, 27, 10, 9]
stepScale = 16000
turns = 50
camera = PiCamera()

# V1 Camera
# camera.resolution = (2592, 1944)
# camera.vflip = True
# camera.hflip = True

# V2 Camera
camera.resolution = (3280, 2464)

folder_time = str(int(time.time()))
os.mkdir(folder_time)
with stp.Motor(M1_pins) as M1:
    for i in range(turns):
        print(i)
        M1.move(int(stepScale / turns))
        M1.release()
        camera.start_preview()
        # Camera warm-up time
        time.sleep(2)
        photoName = '%s/%s.jpg' % (folder_time, str(int(time.time())) )
        camera.capture(photoName)

        # Opens a image in RGB mode 
        im = Image.open(photoName)   

        # Setting the points for cropped image 
        left = 295
        top = 50
        right = 2384
        bottom = 2300

        im1 = im.crop((left, top, right, bottom))
        im.close()
        im1.save(photoName)

