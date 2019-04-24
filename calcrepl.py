import code
import math

#usage: create object with "calc()"
#then call functions with "calc.func(x, y)"

class Calc:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return float(a / b)

    def factorial(self, a):
        r = 1
        for i in range(1, a + 1):   #python loops not inclusive
            r *= i

        return r

    def ncr(self, a, b):
        n = self.factorial(a)
        d = self.mul(self.factorial(a), self.factorial(self.sub(a, b)))
        return self.div(n, d)
        

def calc_repl():
    c = Calc()
    code.interact(
        banner="CSAER CLI Calculator. Ctrl-D to quit.",
        local={"calc": c},
        exitmsg="Bye!"
    )

if __name__ == "__main__":
    calc_repl()
