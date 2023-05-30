from _thread import *
import time

def print_time (threadName, delay):
    count = 0
    while count < 3:
        time.sleep(delay)
        count += 1
        print(threadName, "-------------", time.ctime())

try:
    start_new_thread(print_time, ("thread1", 1))
    start_new_thread(print_time, ("thread2", 2))
except:
    print("this is an error")

while 1:
    pass