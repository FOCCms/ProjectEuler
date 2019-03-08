sumOfSquares = 0
sumOfNubers = 0
for i in range(101):
    sumOfNubers += i
    sumOfSquares += i**2
print(sumOfNubers**2 - sumOfSquares)
