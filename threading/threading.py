import threading
import time

def print_time (threadName, delay):
    count = 0
    while count < 3:
        time.sleep(delay)
        count += 1
        print(threadName, "-------------", time.ctime())

t1 = threading.Thread(target = print_time, args = ("thread1", 1))
t2 = threading.Thread(target = print_time, args= ("thread2", 2))

t1.start()
t2.start()

t1.join()
t2.join()

print("done")