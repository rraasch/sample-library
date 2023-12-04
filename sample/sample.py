#this is a sample of functions to use
import os

def print_hi():
    print('HI!')
    print('*'*10)

def print_list(x0, y0):
    print('Start at', x0)
    print('end at', y0)
    l = range(x0, y0)
    print(l)
    return l

def print_wd():
    print(os.getcwd())
