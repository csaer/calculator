def divide(dividen,divisor):
  quotient = 0
  if type(dividen) == int and type(divisor) == int:
    while dividen:
       dividen -= divisor
       quotient += 1
  else:
    quotient = dividen/divisor;
  return quotient
