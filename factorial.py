#this allows us to import the function multiply from the mult.py file
from mult import multiply   
from subtract import subtract  


# Factorial
#Author: Kyle Zalewski
#This function takes one integer argument, the number for which the calling routine
# expects the factorial returned
# return value is of type integer

def factorial( n ):
		m = subtract(n,1)

		#while loop to iteratively calculate factorial
		while m > 0:
			n = multiply(n, m)
			m = subtract(m,1)

		#return calculated factorial
		return n
