from __future__ import print_function
from fractions import Fraction
import operator

def product(fracs):
    t=reduce(operator.mul , fracs)# complete this line with a reduce statement
    
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(input()):
        fracs.append(Fraction(*map(int, raw_input().split())))
    result = product(fracs)
    print(*result)
