import multiprocessing
import random
import time

def whoami():
    time.sleep(random.random())
    print("Current time:", time.ctime())

if __name__ == "__main__":
    for n in range(3):
        p = multiprocessing.Process(target=whoami)
        p.start()
