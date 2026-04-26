def F(n):
    if n < 2:
        return 1

    if n >= 2 and n % 3 == 0:
        return F(n / 3) - 1

    if n >= 2 and n % 3 != 0:
        return F(n - 1) + 7


for n in range(1, 10000):
    if F(n) == 99:
        print(n)
        break

# 6560
