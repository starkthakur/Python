import threading


class MyThread(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.current_thread().getName())


x = MyThread(name='send message')
y = MyThread(name='receive message')
x.start()
y.start()
