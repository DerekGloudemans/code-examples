# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 16:47:54 2019

@author: derek
"""


import zmq
import random
import time
import queue
from PIL import Image
import _pickle as pickle
import multiprocessing as mp
import threading
import numpy as np

"""
The goal is for a process to share its own copy of var with its threads that it calls,
without affecting other process copies of that variable
"""

def thread_fn(new_val):
    global var
    print ("Thread {} knows that var is {}".format(new_val,var))
    
def process_fn(new_val):
    global var
    var = new_val
    t2 = threading.Thread(target = thread_fn, args = (new_val))
    t2.start()
    t2.join()


if __name__== "__main__":
    var = 0    
    t = threading.Thread(target = thread_fn, args = (-1,))
    t.start()
    t.join()

    jobs = []
    for i in range(0,5):
        p = mp.Process(target = process_fn, args = (i,))
        p.start()
        jobs.append(p)
    for p in jobs:
        p.join()
    
    t = threading.Thread(target = thread_fn, args = (-1,))
    t.start()
    t.join()
    