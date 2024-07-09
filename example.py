from machine import Pin, PWM
from sv_lib import servo

sv = servo.Servo()
servo  = PWM(Pin(15))

servo.freq(50)
servo.duty_u16(sv.Deg(180,0))