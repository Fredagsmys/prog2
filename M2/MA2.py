"""
Solutions to module 2 - A calculator
Student: Max Mattsson
Mail:max.mattsson00@gmail.com
Reviewed by: Mikael Johansson
Reviewed date: 2022-09-23
"""

"""
Note:
The program is only working for a very tiny set of operations.
You have to add and/or modify code in ALL functions as well as add some new functions.
Use the syntax charts when you write the functions!
However, the class SyntaxError is complete as well as handling in main
of SyntaxError and TokenError.
"""

import math
from tokenize import TokenError
from MA2tokenizer import TokenizeWrapper


class SyntaxError(Exception):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)


class EvaluationError(Exception):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)


def log(val):
    if val <= 0:
        raise EvaluationError("Logarithm of non-positive value is not defined")

    result = math.log(float(val))
    return result


def sin(val):
    result = math.sin(float(val))
    return result


def cos(val):
    result = math.cos(float(val))
    return result


def exp(val):
    result = math.exp(float(val))
    return result


def sum(args):
    _sum = 0
    for n in args:
        _sum += n
    return _sum


def mean(args):
    result = sum(args) / len(args)
    return result


def fib(_val):
    cache = {0: 0, 1: 1}

    def _fib(val):
        if val < 0:
            raise EvaluationError("Only positive values allowed")
        elif val % 1 != 0:
            raise EvaluationError("Only integer values allowed")
        if val in cache:
            return cache.get(val)

        cache[val] = _fib(val - 1) + _fib(val - 2)
        return cache[val]

    return _fib(_val)


def fac(val):
    if val < 0:
        return EvaluationError("Negative numbers not allowed")
    elif val % 1:
        raise EvaluationError("Not integer")
    elif val == 0:
        return 1
    result = fac(val - 1) * val
    return result


functions_1 = {"sin": sin, "exp": exp, "log": log, "cos": cos, 'fib': fib, 'fac': fac}
functions_n = {"sum": sum, "mean": mean, "min": min, "max": max}
variables = {"ans": 0.0, "E": math.e, "PI": math.pi}


def statement(wtok, variables):
    """ See syntax chart for statement"""

    result = assignment(wtok, variables)
    if wtok.is_at_end():
        pass
    else:
        raise SyntaxError("EOL error")
    return result


def assignment(wtok, variables):
    """ See syntax chart for assignment"""

    result = expression(wtok, variables)
    while wtok.get_current() == '=':
        wtok.next()
        if wtok.is_name():
            variables[wtok.get_current()] = result
            wtok.next()
        else:
            raise SyntaxError("Expected variable name")
    return result


def expression(wtok, variables):
    """ See syntax chart for expression"""

    result = term(wtok, variables)
    while wtok.get_current() == '+' or wtok.get_current() == '-':
        tok = wtok.get_current()
        wtok.next()
        if tok == '+':
            result = result + term(wtok, variables)
        elif tok == '-':
            result = result - term(wtok, variables)
    return result


def term(wtok, variables):
    result = factor(wtok, variables)
    while wtok.get_current() == "*" or wtok.get_current() == "/":
        wtok.next()
        if wtok.get_previous() == '*':
            result *= factor(wtok, variables)
        elif wtok.get_previous() == '/':
            fac = factor(wtok, variables)
            if fac != 0:
                result /= fac
            else:
                raise EvaluationError("")

    return result


def arglist(wtok, variables):
    rlist = []

    def _arglist(wtok, variables):
        if wtok.get_current() == "(":
            wtok.next()
            rlist.append(assignment(wtok, variables))
            _arglist(wtok, variables)

        elif wtok.get_current() == ",":
            wtok.next()
            rlist.append(assignment(wtok, variables))
            _arglist(wtok, variables)

        elif wtok.get_current() == ")":
            return rlist

        else:
            raise SyntaxError("Expected , or )")

    _arglist(wtok, variables)
    return rlist


def factor(wtok, variables):
    func_1 = functions_1.get(wtok.get_current())
    func_n = functions_n.get(wtok.get_current())
    var = variables.get(wtok.get_current())
    if wtok.get_current() == '(':
        wtok.next()
        result = assignment(wtok, variables)
        if wtok.get_current() != ')':
            raise SyntaxError("Missing right parentheses")
        else:
            wtok.next()

    elif wtok.is_number():
        result = float(wtok.get_current())
        wtok.next()

    elif wtok.get_current() == '-':
        wtok.next()
        result = - term(wtok, variables)

    elif wtok.is_name():
        if var is not None:
            result = float(var)
            wtok.next()
        elif wtok.get_current() in functions_1:
            wtok.next()
            if wtok.get_current() == '(':
                result = func_1(factor(wtok, variables))

            else:
                raise SyntaxError("Expected start parentheses")

        elif wtok.get_current() in functions_n:

            wtok.next()
            rlist = arglist(wtok, variables)
            result = func_n(rlist)
            wtok.next()
        else:
            raise EvaluationError(wtok.get_current() + " is not recognized name")

    else:
        raise SyntaxError("Not allowed operation")
    return result


def main():
    """
    Handles:
       the iteration over input lines,
       commands like 'quit' and 'vars' and
       raised exceptions.
    Starts with reading the init file
    """

    print("Numerical calculator")

    # Note: The unit test file initiate variables in this way. If your implementation
    # requires another initiation you have to update the test file accordingly.
    init_file = 'C:/Users/maxma/PycharmProjects/pythonProject1/prog2/M2/MA2init.txt'
    lines_from_file = ''
    try:
        with open(init_file, 'r') as file:
            lines_from_file = file.readlines()

    except FileNotFoundError:
        print(f"File {init_file} not found")

    while True:
        if lines_from_file:
            line = lines_from_file.pop(0).strip()
            print('init  :', line)
        else:
            line = input('\nInput : ')
        if line == '' or line[0] == '#':
            continue
        wtok = TokenizeWrapper(line)

        if wtok.get_current() == 'quit':
            print('Bye')
            exit()
        elif wtok.get_current() == "vars":
            for key in variables.keys():
                print(f"{key} = {variables.get(key)}")
        else:
            try:

                result = statement(wtok, variables)
                print(result)
                variables['ans'] = result
                print('Result:', result)

            except SyntaxError as se:
                print("*** Syntax error: ", se)
                print(
                    f"Error occurred at '{wtok.get_current()}' just after '{wtok.get_previous()}'")

            except TokenError as te:
                print('*** Syntax error: Unbalanced parentheses')

            except EvaluationError as ee:
                print('*** Evaluation error: Division by zero')


if __name__ == "__main__":
    main()
