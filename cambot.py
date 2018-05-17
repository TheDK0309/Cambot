import webiopi
GPIO = webiopi.GPIO

# Left motor GPIOs
L1=9 # L293 IN1 on GPIO 9
L2=10 # L293 IN2 on GPIO 10
LS=11 # L293 EN1 on GPIO 11
# Right motor GPIOs
R1=23 # L293 IN3 on GPIO 23
R2=24 # L293 IN4 on GPIO 24
RS=25 # L293 EN2 on GPIO 25

# Instantiate WebIOPi server
server = webiopi. Server(port=8000,login="cambot",password="cambot")
# Run the default loop
webiopi. runLoop()
# Cleanly stop the server
server. stop()
def left_stop():
	GPIO. output(L1, GPIO.LOW)
	GPIO. output(L2, GPIO.LOW)
def left_forward():
	GPIO. output(L1, GPIO.HIGH)
	GPIO. output(L2, GPIO.LOW)
def left_backward():
    GPIO.output(L1, GPIO.LOW)
    GPIO.output(L2, GPIO.HIGH)

# Right motor functions
def right_stop():
	GPIO. output(R1, GPIO.LOW)
	GPIO. output(R2, GPIO.LOW)
def right_forward():
	GPIO. output(R1, GPIO.HIGH)
	GPIO. output(R2, GPIO.LOW)
def right_backward():
    GPIO.output(R1, GPIO.LOW)
    GPIO.output(R2, GPIO.HIGH)

# Set the motors speed
def set_speed(speed):
	GPIO. pulseRatio(LS, speed)
	GPIO. pulseRatio(RS, speed)
# Movement functions
def go_forward():
	left_forward()
	right_forward()
def stop():
	left_stop()
	right_stop()
def go_backward():
    left_backward()
    right_backward()
def turn_left():
    right_forward()
    left_backward()
def turn_right():
    right_backward()
    left_forward()
	
# Setup GPIOs
GPIO.setFunction(LS, GPIO.PWM)
GPIO.setFunction(L1, GPIO.OUT)
GPIO.setFunction(L2, GPIO.OUT)
GPIO.setFunction(RS, GPIO.PWM)
GPIO.setFunction(R1, GPIO.OUT)
GPIO.setFunction(R2, GPIO.OUT)
set_speed(0.5)
stop()

server. addMacro(go_forward)
server. addMacro(stop)
server. addMacro(go_backwardward)
server. addMacro(turn_left)
server. addMacro(turn_right)