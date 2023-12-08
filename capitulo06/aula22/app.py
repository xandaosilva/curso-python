from time import sleep
from threading import Thread

class MyThread(Thread):
    def __init__(self, text, time):
        self.text = text
        self.time = time
        super().__init__()

    def run(self):
        sleep(0.5)
        print(self.text)


th1 = MyThread("Thread 1", 2)
th1.start()

th2 = MyThread("Thread 2", 3)
th2.start()

th3 = MyThread("Thread 3", 5)
th3.start()

for i in range(11):
    print(i)
    sleep(1)
