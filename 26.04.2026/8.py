F = [0] * 100

for n in range(100):
    if n <= 1:
        F[n] = 1

    elif n > 1 and n % 2 == 0:
        F[n] = 11 * n + F[n - 1]

    else:
        F[n] = 11 * F[n - 2] + n


summ = 0

for i in F[35:51]:
    if i % 2 == 0:
        summ += i

print(len(str(summ)))

# 25
