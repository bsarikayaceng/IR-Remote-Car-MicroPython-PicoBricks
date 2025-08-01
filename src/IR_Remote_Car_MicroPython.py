# Import necessary modules for PicoBricks and ESP32
from machine import Pin, I2C
from picobricks import MotorDriver, NEC_16, IR_RX, HCSR04
import utime

# Motor speed value (0–255)
SPEED = 150

# Initialize I2C connection (SCL on GPIO 22, SDA on GPIO 21)
i2c = I2C(0, scl=Pin(22), sda=Pin(21))

# Create motor driver object
motor = MotorDriver(i2c)

# IR remote setup
ir_data = 0
data_rcvd = False
current_direction = "stopped"  # Tracks current direction

# IR callback function
def ir_callback(data, addr, ctrl):
    global ir_data, data_rcvd
    if data > 0:
        ir_data = data
        data_rcvd = True

# Initialize IR receiver on pin 17 with NEC protocol
ir = NEC_16(Pin(17, Pin.IN), ir_callback)

# Movement functions
def forward():
    global current_direction
    motor.dc(1, SPEED, 0)
    motor.dc(2, SPEED, 0)
    current_direction = "forward"
    print("Moving forward...")

def backward():
    global current_direction
    motor.dc(1, SPEED, 1)
    motor.dc(2, SPEED, 1)
    current_direction = "backward"
    print("Moving backward...")

def left():
    global current_direction
    motor.dc(1, SPEED, 1)
    motor.dc(2, SPEED, 0)
    current_direction = "left"
    print("Turning left...")

def right():
    global current_direction
    motor.dc(1, SPEED, 0)
    motor.dc(2, SPEED, 1)
    current_direction = "right"
    print("Turning right...")

def stop():
    global current_direction
    motor.dc(1, 0, 0)
    motor.dc(2, 0, 0)
    current_direction = "stopped"
    print("Stopped.")

# Ultrasonic distance sensor setup (TRIG on 26, ECHO on 27)
hcsr = HCSR04(26, 27)

# Main loop
while True:
    # Measure distance from obstacle
    distance = hcsr.distance_cm()
    print("Distance:", distance, "cm")

    # Stop motors if obstacle is detected while going forward
    if current_direction == "forward" and 0 < distance < 15:
        stop()
        print("Obstacle detected. Stopped.")

    # Check IR remote input
    if data_rcvd:
        data_rcvd = False
        if ir_data == IR_RX.number_up:
            forward()
        elif ir_data == IR_RX.number_down:
            backward()
        elif ir_data == IR_RX.number_left:
            left()
        elif ir_data == IR_RX.number_right:
            right()
        elif ir_data == IR_RX.number_ok:
            stop()
        else:
            print("Unknown button:", hex(ir_data))

    utime.sleep_ms(150)
