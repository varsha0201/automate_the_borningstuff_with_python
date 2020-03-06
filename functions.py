# ------------------------------random function
import random
rn =random.randint(1,10)
print(rn)

# -------------------------------sys function

import sys
print('Hello')
sys.exit()
print('Good Bye')

# ------------------------------- pyperclip
import pyperclip

pyperclip.copy('Hello World')
pyperclip.paste()

# -------------------------------User-define funtion
def hello():
    print('Hello')
    print('Hi')
    print('Helloooo')
hello()
hello()
hello()

#---------------------------------- function arguments

def hello1(name):
    print('Hello ' + name)

hello1('bob')
hello1('Alice')

def pluseOne(number):
    return number +1

newnumber = pluseOne(5)
print(newnumber)