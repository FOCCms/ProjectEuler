multiple = 11 * 13 * 17 * 19
divList = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
lst = []
for i in range(multiple*20*18*16, multiple, -1):
    for div in divList:
        if i % div != 0:
            break
    else:
        lst.append(i)
print(lst)
