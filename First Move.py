from gpiozero import Robot
import time

robot = Robot(left=(17,18), right=(27,22))

for i in range(4):
	robot.forward()
	time.sleep(0.5)
	robot.right()
	time.sleep(0.25)
