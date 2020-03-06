name = 'Alice'
if name == 'Alice':
    print('Hi Alice')
print('Done')

# --------------------If else---------------------------------------------------------
password = 'test12'
if password== 'test':
    print('True')
else:
    print('Wrong password')

#-------------------if elif -----------------------------------------------------------
name = 'Bob'
age =3000

if name=='Alice':
    print('Hi Alice')
elif age < 20:
    print('You are not Alice.')
elif age > 2000:
    print('Unlike you, alice is not an undead, immortal vamprie.')
elif age> 100:
    print('You are not Alice, grannie,')

print('Enter a name:')
name = input()
if name:
    print('Thank you for enterning a name.')
else:
    print('You did not enter name.')