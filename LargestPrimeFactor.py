# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

import math

number = 600851475143
factorsList = []

# find all factors of number
for i in range(1, math.ceil(math.sqrt(number))):
    if number % i == 0:
        factorsList.append(int(i))
        factorsList.append(int(number / i))
factorsList.sort(reverse=True)

# pop 1 and "number"
factorsList.pop(0)
factorsList.pop()

primeFactorsList = []
for factor in factorsList:
    i = 2
    limit = int(math.sqrt(factor))
    isComposite = False
    while i <= limit:
        if factor % i == 0:
            isComposite = True
            break
        i += 1
    if not isComposite:
        print(factor)
        primeFactorsList.append(factor)
        break
