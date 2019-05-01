from gpiozero import LED
from time import sleep

'''
Pulse A : GPIO 13
Pulse B : GPIO 26
'''

pulseA = LED(13)
pulseB = LED(26)
pulseA.on()
pulseB.on()
sleep(0.05)
pulseA.off()
pulseB.off()

#while True:
    #led.on()
    #sleep(0.05)
    #led.off()
    #sleep(0.05)
