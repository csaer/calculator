
# Factorial
#Author: Kyle Zalewski
#This function takes one integer argument, the number for which the calling routine
# expects the factorial returned
# return value is of type integer

def factorial( n ):
		m = n - 1

		#while loop to iteratively calculate factorial
		while m > 0:
			#uncomment line 16 when multiplication function has been completed
			#rename function call as appropriate
			#comment out line 17
			n = multiply(n, m)
			#n *= m
			#uncomment line 21 when subtraction function has been completed
			#rename/modify function call as appropriate
			#comment out line 22
			#m = subt(m, 1)
			m -= 1

		#return calculated factorial
		return n
