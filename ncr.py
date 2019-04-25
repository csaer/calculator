from mult import multiply   
from subtract import subtract 
from factorial import factorial

#nCr
#B. Tschuy 4-25-19
#Input: numbers a & b
#Output: quantity of combinations of 'a' distinct elements of set [1..b]

def ncr(a, b):
    n = factorial(a)
    d = multiply(factorial(b), factorial(sub(a, b)))
    return self.div(n, d)
