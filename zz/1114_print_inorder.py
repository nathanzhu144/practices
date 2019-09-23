from threading import Lock
from threading import Barrier

import threading

# Implementation with Barriers

class FoowithBarrier:
    def __init__(self):
        self.first_barrier = Barrier(2)
        self.second_barrier = Barrier(2)
            
    def first(self):
        print("First")
        self.first_barrier.wait()
        
    def second(self):
        self.first_barrier.wait()
        print("Second")
        self.second_barrier.wait()
            
    def third(self):
        self.second_barrier.wait()
        print("Third")

    def run(self):
        t1 = threading.Thread(target=self.second)
        t2 = threading.Thread(target=self.first)
        t3 = threading.Thread(target=self.third)
        t2.start()
        t1.start()
        t3.start()

# NOTE: These two are equivalent
# In python, when you use "with" the lock will have to be acquired before
# entering the block, and will be released when entering the block
#
# with self.lock:
#    do something
#
# 
# self.lock.acquire()
# try:
#    do something
# finally:
#    self.lock.release()
# 
class FoowithLock:
    
    def __init__(self):
        self.locktwo = Lock()
        self.lockthree = Lock()
        self.locktwo.acquire()
        self.lockthree.acquire()
    def first(self):
        print("First")
        self.locktwo.release()

    def second(self):
        with self.locktwo:
            print("Second")
            self.lockthree.release()

    def third(self):
        with self.lockthree:
            print("Third")

    def run(self):
        t2 = threading.Thread(target = self.second)
        t3 = threading.Thread(target = self.third)
        t1 = threading.Thread(target = self.first)
        t3.start()
        t2.start()
        t1.start()

from threading import Event
class FoowithEvent:
    def __init__(self):
        self.done = (Event(), Event())

    def first(self):
        print("First")
        self.done[0].set()
    
    def second(self):
        self.done[0].wait()
        print("Second")
        self.done[1].set()

    def third(self):
        self.done[1].wait()
        print("Third")

    def run(self):
        t2 = threading.Thread(target = self.second)
        t3 = threading.Thread(target = self.third)
        t1 = threading.Thread(target = self.first)
        t3.start()
        t2.start()
        t1.start()

from threading import Semaphore
class FoowithSemaphore:
    def __init__(self):
        self.gates = (Semaphore(0), Semaphore(0))

    def first(self):
        print("First")
        self.gates[0].release()

    def second(self):
        with self.gates[0]:
            print("Second")
            self.gates[1].release()

    def third(self):
        with self.gates[1]:
            print("Third")

    def run(self):
        t2 = threading.Thread(target = self.second)
        t3 = threading.Thread(target = self.third)
        t1 = threading.Thread(target = self.first)
        t3.start()
        t2.start()
        t1.start()
if __name__ == "__main__":
    f = FoowithSemaphore()
    f.run()