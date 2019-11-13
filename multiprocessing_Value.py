"""
multiprocessing Value test
"""

import multiprocessing as mp
import time

def worker():
    test = mp.Value('i',10)
    time.sleep(5)
    print("Value is {}".format(test.value))
def worker2():
    test = mp.Value('i',20)
    time.sleep(5)
    print("Value is {}".format(test.value))

if __name__ == "__main__":
    p = mp.Process(target = worker)
    p2 = mp.Process(target = worker2)
    
    p.start()
    p2.start()
    
    p.join()
    p2.join()
    
    