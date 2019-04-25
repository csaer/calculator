
def multiply(x, y):
  prod = 0
  if y % 2 == 0 or y % 2 == 1:
    for i in range(y):
      prod += x
  else:
    prod = x * y

  return prod
