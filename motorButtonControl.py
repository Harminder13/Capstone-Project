import keyboard
import servo
import time

def main():
    s = servo.Servo('COM5', 0)
    s.setAccel(1)
    s.setSpeed(2)
    s.setLimits(1175, 1375)
    print(s.getAttemptedPos())
    while True:
        if keyboard.is_pressed('up'):
            s.setPos(s.getAttemptedPos()+1)
            print(s.getAttemptedPos())
            time.sleep(0.001)
        if keyboard.is_pressed('down'):
            s.setPos(s.getAttemptedPos()-1)
            print(s.getAttemptedPos())
            time.sleep(0.001)
        if keyboard.is_pressed('esc'):
            exit()

main()
