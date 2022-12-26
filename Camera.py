from picamera import PiCamera
##import curses
##from gpiozero import Robot

camera = PiCamera()
camera.resolution = (120, 240)
camera.rotation = 180
camera.start_preview()
