#Dictionary mapping

def switch():
    value1 = int(input('Enter the first value:'))
    value2 = int(input('Enter the second vaue:'))
    print('Press 1 for addition \n 2 for substraction \n 3 for multiplication \n 4 for division')
    option = int(input('Enter your option:'))

    def add():
        result = value1 + value2
        print(result)
    def sub():
        result = value1 - value2
        print(result)
    def mul():
        result = value1 * value2
        print(result)
    def div():
        result = value1 / value2
        print(result)
    
    dictionary ={
        1 : add,
        2 : sub,
        3 : mul,
        4 : div}
    dictionary.get(option)()
switch()