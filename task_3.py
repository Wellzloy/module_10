import time
import threading

print(time.ctime(time.time()))
counter = 0


def increment(name):
    global counter
    for i in range(1000):
        counter += 1
        print((name, counter))

    def decrement(name):
        global counter
        for i in range(1000):
            counter -= 1
            print(name, counter)


thread1 = threading.Thread(target=increment, args=('thread1'))
thread2 = threading.Thread(target=increment, args=('thread2'))
thread3 = threading.Thread(target=increment, args=('thread3'))
thread4 = threading.Thread(target=increment, args=('thread4'))
thread1.start()
thread3.start()
thread2.start()
thread4.start()




