def sum(x, y):
    # print(x+y)
    return x + y


print(sum(4, 5))

# default Parameter


# keyword Argument
def more_num(a, b=7, c=10):
    print("a is", a, "b is", b, "c is ", c)


more_num(2)

# pass statment


def dream_home():
    pass

# varArgs parameter


def total_numbers(a=7, *numbers, **phonebook):
    # the single astric is for tuple and the dounle astric is for dict
    print("My fav nummber is ", a)

    for num in numbers:
        print("num", num)

    for name, phone_number in phonebook.items():
        print(name, phone_number)


total_numbers(7, 1, 2, 3, Jane=2222, John=4444, Angela=5555)

# Anonymous Function(Lambda)


def a(b): return b + 4


"""" also the same  
a = lambda b: b +4 
print(a(4))
this called anaymoous function
"""

print(a(4))


def c(d, e): return d + e

"""
c = lambda d,e : d + e
print(c(7,8))
"""
print(c(7, 8))


def new_number(n):
    return lambda f: f * n


double_num = new_number(2)
print(double_num(20))
