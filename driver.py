#!/usr/bin/env python3

import sys
import factorial as f
import traceback

def usage():
	print("This requires 1 argument.\nThe given argument should be a number.")

def main():
    print(sys.argv[1] +'! = ' + str(f.factorial(float(sys.argv[1]))))

if __name__ == '__main__':
	if len(sys.argv) > 1:
		try:
			main()
		except Exception as e:
			traceback.print_exc()
			print("\n")
			usage()

	else:
		usage()
