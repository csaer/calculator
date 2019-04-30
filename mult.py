
def multiply(x, y):
  prod = 0
  if type(y) == int or type(x) == int:
    for i in range(y):
      prod += x
  else:
    prod = x * y

  return prod
