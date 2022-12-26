from picamera import PiCamera

camera = PiCamera()
camera.resolution = (120, 240)
camera.rotation = 180
camera.start_preview()
