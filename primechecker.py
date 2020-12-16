# primechecker

def prime_checker(num):
  is_prime = True
  for n in range(2, num):
    if num % n == 0:
      is_prime = False

  if is_prime:
    print("Yes, a Prime number")
  else:
    print("No, not a Prime number")

p = int(input("Check this number: "))
prime_checker(num=p)