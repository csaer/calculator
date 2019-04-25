#!/usr/bin/env python3

import sys
import factorial as f
import subtract as s
import mult as m

def main():
    print('10! = ' + str(f.factorial(10)))
    print('10 - 5 = ' + str(s.subtract(10,5)))
    print('10 * 50 = ' + str(m.multiply(10,50)))

if __name__ == '__main__':
    main()
