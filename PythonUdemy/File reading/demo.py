# demo.py

import math
import useful_functions as uf

scores = [88, 92, 79, 93, 85]

mean = uf.mean(scores)
curved = uf.add_five(scores)

mean_c = uf.mean(curved)

print("Scores:", scores)
print("Original Mean:", mean, " New Mean:", mean_c)

print(__name__)
print(uf.__name__)

# finding the factorial of 4
num = 6
fac_of_4 = 1
for i in range(num):
    mul = i * fac_of_4
    fac_of_4 += mul

print(fac_of_4)

num = math.factorial(6)
print(num)

# for exponent
num = math.exp(3)
print(num)
# or
num = pow(math.e, 3)
print(num)
