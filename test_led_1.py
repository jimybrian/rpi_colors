from ledstrip import LEDStrip
import time
import random

CLK = 3
DAT = 2

strip = LEDStrip(CLK, DAT)

print("Set Color to Red")
for r in range(50, 100):
    strip.setcolourrgb(r, 0, 0)
    time.sleep(0.05)

print("Set Color to Blue")
for b in range(50, 100):
    strip.setcolourrgb(0, 0, b)
    time.sleep(0.05)
    
print("Set Color to Green")
for g in range(50, 100):
    strip.setcolourrgb(0, g, 0)
    time.sleep(0.05)
    
for ra in range(50, 200):
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    strip.setcolourrgb(r, g, b)
    time.sleep(0.50)

print("Set Color to White")
for w in range(50, 200):
    strip.setcolourrgb(w, w, w)
    time.sleep(0.05)
    
print("Switch off lights")
strip.setcolouroff()