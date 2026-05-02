from turtle import *
from itertools import product


def to_5(x):
    s = ''

    while x > 0:
        s += str(x % 5)
        x //= 5

    return s[::-1]

def task_2():
    print('x y z w')

    for x in range(2):
        for y in range(2):
            for z in range(2):
                for w in range(2):
                    if not(y <= x) and not(not(w) and z) and not(x and w):
                        print(x, y, z, w)

def task_5():
    for n in range(100, 49, -1):
        n5 = to_5(n)

        if n % 5 == 0:
            n5 = n5[0] + n5 + n5[-1]
        else:
            n5 += to_5(sum(map(int, n5)))

        r = int(n5, 5)

        if r % 5 == 0:
            print(r)
            break

def task_6():
    screensize(2000, 2000)
    pendown()

    k = 100

    right(90)

    begin_fill()
    for i in range(3):
        forward(15 * k)
        right(60)
        forward(10 * k)
        right(60)
    end_fill()

    canvas = getcanvas()

    count = 0
    for x in range(-500, 500):
        for y in range(-500, 500):
            if canvas.find_overlapping(x * k, y * k, x * k, y * k) == (5, ):
                count += 1

    print(count)

def task_7():
    k1 = (3840 * 2160 * 24 * 8192) // (32 * 2 ** 30 * 8) + 1

    print(k1)

def task_8():
    alph = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
    count = 0

    res = 0

    for i in product(alph, repeat=6):
        count += 1
        wd = ''.join(i)

        if count % 2 == 0:
            res += 1

            if wd == 'СМИТАП':
                print(res)
                break

def task_9():
    with open('04.05.2026/9.txt', 'r') as file:
        res = 0

        for line in file:
            nums = sorted(map(int, line.split()))

            povt = [i for i in nums if nums.count(i) > 1]
            np = [i for i in nums if nums.count(i) == 1]

            if len(povt) == 2 and len(np) == 4:
                if sum(np) % povt[0] == 0:
                    res = sum(nums)

    print(res)

def task_14():
    maxx = -1

    for x in range(1, 4000):
        a = 5 ** 17 + 5 ** 12 - x
        count = 0

        while a > 0:
            if a % 5 == 0:
                count += 1
            
            a //= 5

        maxx = max(maxx, count)    

    print(maxx)

def task_15():
    P = [i / 10 for i in range(150, 301)]
    Q = [i / 10 for i in range(600, 801)]
    A = [i / 10 for i in range(0, 5001)]

    for x in range(5001):
        x = x / 10

        if not(not(not(not(x in A) or (x in P))) or (not(not(x in A) or (not(x in Q))))):
            A.remove(x)

    print(int(A[-1] - A[0]))


task_2()
task_5()
task_6()
task_7()
task_8()
task_9()
task_14()
task_15()

# x y z w
# 0 1 0 0
# 0 1 0 1
# 0 1 1 1

# 3000
# 392
# 6
# 360099094
# 72
# 10
# 65
