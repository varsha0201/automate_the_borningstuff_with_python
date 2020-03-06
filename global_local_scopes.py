spam = 42

def eggs():
    spam = 42
print('This is code')
print('This is something')
#---------------------------------------------------
def spam1():
    eggs = 99
    bacon()
    print(eggs)

def bacon():
    print('inside bacon')

spam1()