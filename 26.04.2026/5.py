F = [0] * 500

for n in range(1, 500):
    if n < 2:
        F[n] = 1
    
    if n >= 2 and n % 4 == 0:
        F[n] = F[n // 4] - 1

    if n >= 2 and n % 4 != 0:
        F[n] = F[n - 1] + 1


print(max(F[100:201]))

# 8
