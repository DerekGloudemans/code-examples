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

def thread_fn():
    global var
    print ("Thread function knows that var is {}".format(var))
    
def process_fn():
    global var
    var = 1
    t2 = threading.Thread(target = thread_fn)
    t2.start()
    t2.join()

if __name__== "__main__":
    var = 0    
    t = threading.Thread(target = thread_fn, args = ())
    t.start()
    t.join()
    
    p = mp.Process(target = process_fn)
    p.start()
    p.join()
    
    t = threading.Thread(target = thread_fn, args = ())
    t.start()
    t.join()
    