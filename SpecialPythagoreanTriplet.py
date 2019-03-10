for a in range(500):
    for b in range(500):
        if a*a+b*b == (1000-a-b)**2:
            print(a * b * (1000-a-b))
            exit()
