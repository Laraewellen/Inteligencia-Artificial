import time
import os
for h in range (1, 24):
    for m in range(1, 60):
        for s in range(1, 60):
            print("h: ", h, "m: ", m, "s: ", s)
            time.sleep(1)
            os.system("cls")