import time
import RPi.GPIO as GPIO

# Set GPIO mode and define pin numbers
GPIO.setmode(GPIO.BCM)

switch1_pin = 15
switch2_pin = 13
led1_pin = 35
led2_pin = 37

# Setup GPIO pins
GPIO.setup(switch1_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(switch2_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(led1_pin, GPIO.OUT)
GPIO.setup(led2_pin, GPIO.OUT)

try:
    while True:
        # Read switch inputs
        switch1_state = GPIO.input(switch1_pin)
        switch2_state = GPIO.input(switch2_pin)

        # Control LED1 based on switch1 state
        if switch1_state == GPIO.LOW:
            GPIO.output(led1_pin, GPIO.HIGH)
        else:
            GPIO.output(led1_pin, GPIO.LOW)

        # Control LED2 based on switch2 state
        if switch2_state == GPIO.LOW:
            GPIO.output(led2_pin, GPIO.HIGH)
        else:
            GPIO.output(led2_pin, GPIO.LOW)

        # Add a small delay to avoid rapid state changes
        time.sleep(3)

except KeyboardInterrupt:
    pass

finally:
    # Cleanup GPIO settings
    GPIO.cleanup()
