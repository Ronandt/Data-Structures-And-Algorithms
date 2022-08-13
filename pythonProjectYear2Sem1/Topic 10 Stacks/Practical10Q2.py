from ast import expr
from cmath import exp
import Stack as Stack
import math
print("Postfix Expression Evaluator")
print("For Help, type 'help' or '?' ")
print("To Quit type 'quit' or 'q' ") 

while True:
    expression = input("Enter a postfix expression to be evaluated: ")
    tokens = expression.split(" ") # Split the expression into tokens
                                    # Seperated by space
                                    # Create an instance of the Stack Object

    myStack = Stack.stack()

    # Handle help option
    if tokens[0] == "help" or tokens[0] == "?":
        print('Postfix Expression Evaluator takes in a mathematical expression \ expressed in Postfix notation and evaluates it.') 
        print('Example: \"1 2 + 4 *\" will evaluate to \"12\"') 
        # Handle quit option 
    elif tokens[0] == "quit" or tokens[0] == "q":
        break
    # Handle Postfix expression entered

    else:
        valid = True
        while len(tokens) > 0:
            token = tokens.pop(0)
            if token.isdigit():
                myStack.push(int(token))
            elif token == "+":
                if myStack.size() > 1:
                    myStack.push(myStack.pop() + myStack.pop())
                else:
                    valid = False
                    break
            elif token == "-":
                if myStack.size() > 1:
                    myStack.push(myStack.pop() - myStack.pop())
                else:
                    valid = False
                    break
            elif token == "*":
                if myStack.size() > 1:
                    myStack.push(myStack.pop() * myStack.pop())
                else:
                    valid = False
                    break
            elif token == "/":
                if myStack.size() > 1:
                    myStack.push(myStack.pop() / myStack.pop())
                else:
                    valid = False
                    break
            elif token == "^":
                if myStack.size() > 1:
                    myStack.push(myStack.pop() ** myStack.pop())
                else:
                    valid = False
                    break
            # elif token == "!":
            #     if myStack.size() < 1:
            #         valid = False
            #         break
            #     else:
            #         num1 = myStack.pop()
            #         myStack.push(factorial(num1))
            elif token == "sin+":
                if myStack.size() > 1:
                    myStack.push(math.sin(math.radians(myStack.pop())) + math.sin((math.radians(myStack.pop()))))
                else:
                    valid = False
                    break
            elif token == "cos+":
                if myStack.size() > 1:
                    myStack.push(math.cos(math.radians(myStack.pop())) + math.cos((math.radians(myStack.pop()))))
                else:
                    valid = False
                    break
            else:
                valid = False
                break
        
        if valid:
            print("Evaulation Result: ", myStack.pop())
        else:
            print("Invalid Postfix Expression")
