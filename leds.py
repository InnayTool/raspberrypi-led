import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT) # PWM pin set as output
pwm = GPIO.PWM(17, 200)  # Initialize PWM on pwmPin 100Hz frequency
GPIO.setup(22, GPIO.OUT)
pwm.start(10)
n = 0
while 1:
	n+=1
