from sys import getsizeof
# example of generator compare to list comhperentio
values = [x*2 for x in range(1000)]
print(getsizeof(values))
# for x in values:
#     print(x)
# lets look for generator both with list comp work same but d/t of memory size
print("\n This is generator")
values = (x*2 for x in range(1000))
print(getsizeof(values))
for x in values:
    print(x)
