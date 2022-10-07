"""
A very small calculator that only handles +, * and ( )

Note that it will give the correct priority to the operations.
Also note the usage of next! Missing call (or to many call)
to next is probbaly the most common problem students have with
the assignment.

You can use the program to see whats happens with incorrect
expressions.

"""
from tokenize import TokenError

from MA2tokenizer import TokenizeWrapper


class MySyntaxError(Exception):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)





def expression(wtok):
    result = term(wtok)
    while wtok.get_current() == '+' or wtok.get_current() == '-':
        tok = wtok.get_current()
        wtok.next()
        if tok == '+':
            result = result + term(wtok)
        elif tok == '-':
            result = result - term(wtok)
    return result


def term(wtok):
    result = factor(wtok)
    while wtok.get_current() == "*" or wtok.get_current() == "/":
        tok = wtok.get_current()
        wtok.next()
        if tok == '*':
            result *= factor(wtok)
        elif tok == '/':
            result /= factor(wtok)

    return result


def factor(wtok):
    if wtok.get_current() == '(':
        wtok.next()  # bypass (
        result = expression(wtok)
        if wtok.get_current() == ')':
            wtok.next()  # bypass )
        else:
            pass

    elif wtok.is_number():  # should be a number
        result = float(wtok.get_current())
        wtok.next()  # bypass the number

    else:
        raise MySyntaxError("Unexpected token from factor")

    return result


def main():
    print("Very simple calculator")

    while True:
        line = input("Input : ")
        wtok = TokenizeWrapper(line)
        try:
            if wtok.get_current() == "quit":
                break
            else:
                result = expression(wtok)
                if wtok.is_at_end():
                    print("Result: ", result)
                else:
                    raise MySyntaxError('Unexpected token')
        except MySyntaxError as se:
            print("*** SyntaxError: ", se.arg)
            print(f"error occured at {wtok.get_current()}, after {wtok.get_previous()}")
        except TokenError:
            print('*** Syntax: Unbalanced parentheses ')

    print("Bye!")


if __name__ == '__main__':
    main()
