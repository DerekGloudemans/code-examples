"""
Multiprocessing Value objects (without locks, which are optionally implemented
so this code is not really safe). The main takeaway is that the multiprocessing 
Value defined outside of the worker functions is shared between each, whereas the
mp value defined within the processes is not, even though it has the same name 
(defined in different namespaces)
"""

import multiprocessing as mp
import time

def worker(test2):
    test = mp.Value('i',10)
    test2.value += 200
    time.sleep(5)
    print("Worker 1: value is {}, shared value is {}".format(test.value,test2.value))

def worker2(test2):
    test = mp.Value('i',20)
    time.sleep(5)
    print("Worker 2: value is {}, shared value is {}".format(test.value,test2.value))

if __name__ == "__main__":
    test2 = mp.Value('i',30)
    p = mp.Process(target = worker, args = (test2,))
    p2 = mp.Process(target = worker2, args = (test2,))
    
    p.start()
    p2.start()
    
    p.join()
    p2.join()
    
    # output:
    # Worker 1: value is 10, shared value is 230
    # Worker 2: value is 20, shared value is 230