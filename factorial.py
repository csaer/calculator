#fact.py
#Author: Kyle Zalewski
#This function takes one integer argument, the number for which the calling routine
# expects the factorial returned
# return value is of type integer

def fact( n ):
		m = n - 1
		
		#while loop to iteratively calculate factorial
		while m > 0:
			#uncomment line 13 when multiplication function has been completed
			#rename function call as appropriate
			#comment out line 16
			#n = mult(n, m)
			n *= m
			#uncomment line 20 when subtraction function has been completed
			#rename/modify function call as appropriate
			#comment out line 21
			#m = subt(m, 1)
			m -= 1
		
		#return calculated factorial
		return n
