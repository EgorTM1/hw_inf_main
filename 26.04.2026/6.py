F = [0] * 3000

for n in range(3000):
    if n == 0:
        F[n] = 0

    if n > 0 and n % 2 == 0:
        F[n] = F[n // 2] - 1

    if n > 0 and n % 2 != 0:
        F[n] = 1 + F[n - 1]

print(sum([1 for i in F[:1000] if i == 0]))

# 41
