# ---------------------while - break
name = ''
while True:
    print('Please eneter your name.')
    name = input()
    if name == 'your name':
        break
print('Thank you')
#------------------------while -continue  ---------------
spam = 0
while spam < 5:
    spam = spam+1
    if spam ==3:
        continue
    print('spam is'+ str(spam))