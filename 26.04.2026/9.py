F = [0] * 3000

for n in range(3000):
    if n <= 1:
        F[n] = 1

    elif n > 1 and n % 2 == 0:
        F[n] = 11 * n * F[n - 1]

    else:
        F[n] = 10 * F[n - 2]


print(F[2024] // F[2020])

# 100
