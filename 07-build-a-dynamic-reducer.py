import operator
from functools import reduce

def flexible_counter(collection, op):
    operators = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
    }

    return reduce((lambda total, element: operators[op](total, element)), collection)

total = flexible_counter([10, 10], '*') # 0.16666666666666666

print( "\n" + "\n" + str(total))