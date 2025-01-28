import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def timer(self):
        wars = 100
        day = 1
        while wars:
            time.sleep(1)
            wars -= self.power
            print(f'{self.name} сражается {day} осталось {wars} войнов')
            day += 1
        print(f'{self.name} одержал победу спустя {day - 1} дней!')

   

    def run(self):
        print(f'{self.name}, на нас напали!')
        self.timer()



first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print("Все битвы закончились!")
