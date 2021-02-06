# Args and Kwargs explained

# *******************************************
# Sample code covering args and kwargs
# values taken into args are stored as tuples
# values taken into kwargs are stored as dictionary
def all_aboard(a, *args, **kw): 
    print(a, args, kw)
 
all_aboard(4, 7, 3, 0, x=10, y=64)
# output is 4 (7,3,0) {'x': 10, 'y': 64}
# *******************************************



# *args: Positional Variable-Length Arguments
# values taken into args are stored as tuples
def add(*args):
    # print(args[1])

    sum = 0
    for n in args:
        sum += n
    return sum
# print(add(3, 5, 6, 2, 1, 7, 4, 3))


# **kwargs: Keyworded Variable-Length Arguments
# values taken into kwargs are stored as dictionary
def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    # print(n)

# this call will take 2 as first argument
# and 3,5 as kwargs
calculate(2, add=3, multiply=5)


# How to use a **kwargs dictionary safely
class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan", model="Skyline")
print(my_car.model)
