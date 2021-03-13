import time
import random

for i in range(1,11):
    Temp = random.randrange(40,50)
    print("Current Temperature : %5.2f [deg]" %Temp, end='')
    time.sleep(1)

for i in range(1,11):
    Temp = random.randrange(40,50)
    print("Current Temperature : %5.2f [deg]" %Temp)
    time.sleep(1)
