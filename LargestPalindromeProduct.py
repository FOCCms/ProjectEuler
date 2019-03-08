maxValue = 999
minValue = 100

largestPalindrome = 0

for firstMultiplier in range(maxValue, minValue, -1):
    for secondMultiplier in range(maxValue, minValue, -1):
        product = firstMultiplier * secondMultiplier
        if str(product) == str(product)[::-1]:
            if product > largestPalindrome:
                largestPalindrome = product

print(largestPalindrome)

