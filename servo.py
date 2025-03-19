import maestro

class Servo:
    # usb is 'COM1', 'COM2', ect. Channel is 0 through 5 depending on which channel
    # on the servo controller the servo is connected to.
    def __init__(self, usb, channel, upper_limit = 2000, lower_limit = 1000):
        self.usb = usb
        self.chan = channel
        self.upper_limit = upper_limit
        self.lower_limit = lower_limit
        self.servo = maestro.Controller(self.usb)
        self.pos = 1000
        self.servo.setSpeed(self.chan, 5)
        self.servo.setAccel(self.chan, 2)
        self.servo.setTarget(self.chan, self.pos*4)

    # Runs the servo.close() command when the servo is no longer in scope
    def __del__(self):
        if hasattr(self, 'servo'):
            self.servo.close()
            print(f"Servo {self.chan} closed.")

    # Set the speed of the servo. The constructor automatically sets the speed to 5. I'm unsure what the units of 5 are.
    def setSpeed(self, speed):
        self.servo.setSpeed(self.chan, speed)

    # Set the acceleration of the servo. The constructor automatically sets the acceleration to 2.
    # I'm unsure what the units of 2 are.
    def setAccel(self, accel):
        self.servo.setAccel(self.chan, accel)

    # Set the acceleration of the servo. The constructor automatically sets the position to 1000.
    # This number can range from approximately 1000 to 2000. (still figuring out if this is the full range)
    def setPos(self, pos):
        if pos > self.upper_limit:
            pos = self.upper_limit
        if pos < self.lower_limit:
            pos = self.lower_limit
        self.pos = pos
        self.servo.setTarget(self.chan, pos*4)

    # Returns the current position of the servo
    def getPos(self):
        return self.servo.getPosition(self.chan)

    # Returns the value
    def getAttemptedPos(self):
        return self.pos

    # Sets the values that are defined as the upper and lower limits of the motors motion.
    def setLimits(self, low, high):
        self.lower_limit = low
        self.upper_limit = high