# Try except variable

def div42by(divideby):
    try:
        return 42/ divideby
    except ZeroDivisionError:
        print('You tried to divied by 0.')

print(div42by(2))
print(div42by(5))
print(div42by(0))

print('How many cat do you have?')
numCats = input()
try:
    if int(numCats) >= 4:
        print('That is a lot of cats')
    else:
        print('That is not many cats.')
except ValueError:
    print('Please enter values in number.')