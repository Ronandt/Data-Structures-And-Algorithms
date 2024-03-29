from ast import expr
from cmath import exp
import stack as Stack
import math
print("Postfix Expression Evaluator")
print("For Help, type 'help' or '?' ")
print("To Quit type 'quit' or 'q' ") 







import re
from collections import namedtuple

opinfo = namedtuple('Operator', 'precedence associativity')
operator_info = {
    "+": opinfo(0, "L"),
    "-": opinfo(0, "L"),
    "/": opinfo(1, "L"),
    "*": opinfo(1, "L"),
    "!": opinfo(2, "L"),
    "^": opinfo(2, "R"),
}


def tokenize(input_string):
    cleaned = re.sub(r'\s+', "", input_string)
    chars = list(cleaned)

    output = []
    state = ""
    buf = ""

    while len(chars) != 0:
        char = chars.pop(0)

        if char.isdigit():
            if state != "num":
                output.append(buf) if buf != "" else False
                buf = ""

            state = "num"
            buf += char

        elif char in operator_info.keys() or char in ["(", ")"]:
            output.append(buf) if buf != "" else False
            buf = ""

            output.append(char)

        else:
            if state != "func":
                output.append(buf) if buf != "" else False
                buf = ""

            state = "func"
            buf += char

    output.append(buf) if buf != "" else False
    return output


def shunt(tokens):
    tokens += ['end']
    operators = []
    output = []

    while len(tokens) != 1:
        current_token = tokens.pop(0)

        if current_token.isdigit():
            # Is a number
            print("number", current_token)
            output.append(current_token)

        elif current_token in operator_info.keys():
            # Is an operator
            print("op", current_token)

            while True:
                if len(operators) == 0:
                    break

                satisfied = False

                if operators[-1].isalpha():
                    # is a function
                    satisfied = True

                if operators[-1] not in ["(", ")"]:
                    if operator_info[operators[-1]].precedence > operator_info[current_token].precedence:
                        # operator at top has greater precedence
                        satisfied = True

                    elif operator_info[operators[-1]].precedence == operator_info[current_token].precedence:
                        if operator_info[operators[-1]].associativity == "left":
                            # equal precedence and has left associativity
                            satisfied = True

                satisfied = satisfied and operators[-1] != "("

                if not satisfied:
                    break

                output.append(operators.pop())

            operators.append(current_token)

        elif current_token == "(":
            # Is left bracket
            print("left", current_token)
            operators.append(current_token)

        elif current_token == ")":
            # Is right bracket
            print("right", current_token)

            while True:
                if len(operators) == 0:
                    break

                if operators[-1] == "(":
                    break

                output.append(operators.pop())

            if len(operators) != 0 and operators[-1] == "(":
                operators.pop()

        else:
            # Is a function name
            print("func", current_token)
            operators.append(current_token)

    output.extend(operators[::-1])

    return output


while True:
    expression = input("Enter a postfix expression to be evaluated: ")
    tokens = tokenize(expression)
    tokens = " ".join(shunt(tokens))

    tokens = tokens.split(" ") # Split the expression into tokens

                                    # Seperated by space
                                    # Create an instance of the Stack Object
    print(tokens)

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

            else:
                valid = False
                break
        
        if valid:
            print("Evaulation Result: ", myStack.pop())
        else:
            print("Invalid Postfix Expression")
