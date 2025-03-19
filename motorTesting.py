import servo

s1 = servo.Servo('COM5', 0)
s1.setAccel(1)
s1.setSpeed(2)
s1.setLimits(1175, 1375)
s1.setPos(1100)
x = s1.getPos() #get the current position of servo 1
print(x)
