import math

number = 600851475143
factorsList = []

# find all factors of number
for i in range(1, math.ceil(math.sqrt(number))):
    if number % i == 0:
        factorsList.append(int(i))
        factorsList.append(int(number / i))
factorsList.sort()

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
        primeFactorsList.append(factor)

print(primeFactorsList[-1])
