from multiprocessing import Process, Lock
import time

"""
Note that the multiprocessing lock is special in that it is passed by reference between processes,
whereas most objects are required to be serializable (pickleable). 
"""

# Simple function that grabs a lock and waits
def func1(lock):
    lock.acquire()
    time.sleep(10)
    lock.release()

if __name__ == "__main__":
    lock = Lock()
    p = Process(target = func1, args = (lock,))
    
    lock.acquire()
    p.start()
    print("Print number 1.")
    lock.release()
    
    # sleep gives enough time for process p to acquire lock
    time.sleep(1.1)
    
    lock.acquire()
    print("Print number 2. If we had to wait 10 seconds, it's because p had the lock")
    lock.release()
    
    # end process and wait for it to terminate
    p.terminate()
    p.join()