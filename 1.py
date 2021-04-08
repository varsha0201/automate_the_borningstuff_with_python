# input() always return in string.

print('What is your name?')
myName = input() # Enter values in '' quatation. To avoid the error.
print('Hello! ' + myName +' Nice to meet you.')
print(len(myName))
print('What is your age?')
myAge = input()
print(type(myAge))
print("My current age is: "+ str(int(myAge)))