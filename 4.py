#Control statement

# While statement
spam = 0 
while spam < 5:
    print('Hello World')
    spam = spam + 1

# break , continue statements

spam = 0 

while spam < 5:
    spam = spam + 1
    if spam == 3:
        continue
    print('spam is' + str(spam))

row = 0
while row < 100:
    row = row + 1
    if row == 50:
        break
    print(' Row is:' + str(row))
 