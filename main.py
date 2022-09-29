from calc import addition
from calc import subtraction
from calc import multiplication
from calc import division


while True:
    command =(input ('Enter a command from "add", "subtract", "multiply", "divide": '))
    number1 = (float (input('enter your first number: ')))
    number2 = (float (input('enter your second number: ')))
    if command ==('add'):
        print ("number1 ", "+", "number2 ", "=", addition (number1, number2))
    elif command ==('subtract'):
        print ("number1 ", "-", "number2 ", "=",  subtraction (number1, number2))
    elif command==('multiply'):
        print ("number1 ", "*", "number2 ", "=", multiplication (number1, number2))
    elif command == ('divide'):
        print ("number1 ", "/", "number2 ", "=",  division (number1, number2))
    else:
        print ('error')
    Question= (input ('Would you like to make another operation? "yes", "no", "stop"'))
    if Question== ("yes"):
        pass
    elif Question== ("no"):
        break
    elif Question== ("stop"):
        quit ()
    else:
        print ('Error')
        break
