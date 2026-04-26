def is_prime(x):
    if x <= 2:
        return True

    for i in range(2, x):
        if x % i == 0:
            return False


F = [0] * 100

for n in range(100):
    if n < 2:
        F[n] = 1

    elif n > 1 and n % 3 == 0:
        F[n] = 2 * F[n - 1] + F[n - 2]

    else:
        F[n] = 3 * F[n - 2] + F[n - 1]


count = 0

for i in F[1:36]:
    num = sum(map(int, str(i)))

    if is_prime(num):
        count += 1

print(count)

# 1