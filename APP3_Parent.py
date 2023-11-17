from microbit import *
import radio
import music
import time

radio.config(group=22)
radio.on()

for x in range(2):
    music.play(["C4:4", "D4", "E4", "C4"])

for x in range(2):
    music.play(["E4:4", "F4", "G4:8"])
display.scroll("Bienvenue sur Be:TAG")
sleep(5)

while True:
    display.scroll("Press A for settings")
    if button_a.was_pressed():
        display.clear()
        sleep(1000)
        break

