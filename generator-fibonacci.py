# Calcualating FIBONACCI using generator


# GENERATOR version
# generator version gets the value from range and pauses and displays immediately without memory storage
def fib(number):
  a = 0
  b = 1
  for i in range(number):
    yield a
    temp = a
    a = b
    b = temp + b

for x in fib(100):
  print(x)


# LIST version - (normal)
# list version generates number from range and keep it in memory. Hence slower and less efficient
def fib(number):
  a = 0
  b = 1
  result = []
  for i in range(number):
    result.append(a)
    temp = a
    a = b
    b = temp + b
  return result


print(fib2(100))
