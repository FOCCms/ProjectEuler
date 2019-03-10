n = 100
guess = 10001
lst = []
while len(lst) < guess:
    n *= 100
    lst.clear()

    a = list(range(n+1))
    a[1] = 0
    i = 2
    while i <= n:
        if a[i] != 0:
            lst.append(a[i])
            if len(lst) == guess:
                break

            for j in range(i, n+1, i):
                a[j] = 0
        i += 1

print(lst[guess-1])
