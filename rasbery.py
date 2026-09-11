from gpiozero import LED, Buzzer
from time import sleep

led = LED(17)
led2= LED(27)
led3= LED(22)
buzzer= Buzzer(13)

while True:
    led.on()
    buzzer.on()
    sleep(2)
    buzzer.off()
    led2.off()
    led3.off()
    sleep(5)
    
    led.off()
    led2.on()
    led3.off()
    sleep(5)
    
    led.off()
    led2.off()
    led3.on()
    sleep(3)
