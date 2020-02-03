import string
my_car = {
    "brand": "Range Rover Sports",
    "model": "HSE",
    "year": 2017
}
print(my_car.keys())
my_car.clear()
print(my_car)

# Function


def sum(x, y):
    return x + y


print(sum(2, 3))
print(sum(8, 4))


def student_names(names="Bluelime"):
    print("Hello " + names)


student_names()
student_names(names="John")
student_names("Jane")


def more_num(a, b=7, c=10):
    print("a is ", a, "b is", b, "while c is", c)


more_num(3, 7)
more_num(23, c=17)
more_num(c=40, a=80)


x = 10


def my_nummber():
    global x
    print(x)
    x = 7
    print(x)


my_nummber()
print(x)


# creating list
x = [10, 20, 30]
y = x
x[1] = 42
print(y)


# creating dict tuple key value pair
values = {
    ("Ghostbussters", 2016): 5.4,
    ("Ghostbusster", 1984): 7.8,
    ("cars", 2006): 7.1

}
x = values[("cars", 2006)]

print(x)

y = ("cars", 2016) in values
print(y)
z = values.get(("cars", 2006))
print(z)
Sum = values.get(("cars", 2016))
Sum == None
print(Sum)
# values.pop(("cars", 2006))
# print(values)

# Looping in dict
for key, value in values.items():
    print(key, ":", value)

# looping in dict and popin up keys
to_remove = []

for i in values:
    if(i[1]) < 2000:
        to_remove.append(i)

print(to_remove)

for i in to_remove:
    values.pop(i)

print(to_remove)

# List Comprehsion and creating dict

list = {i: i**2 for i in range(1, 11)}
print(list)

alpha= {i:chr(i) for i in range(65,90)}
print(alpha)


# Set
leos_color = set(["blue","yellow","green"])
medex_color = set(["red","blue"])
mixed_color = leos_color.union(medex_color)
common_color = leos_color.intersection(medex_color)
print(common_color)

print(mixed_color)