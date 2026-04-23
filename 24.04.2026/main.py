from turtle import *
from itertools import product


def task_2():
    print('x y z w')

    for x in range(2):
        for y in range(2):
            for z in range(2):
                for w in range(2):
                    if (not(w) and z and not(y) and not(x)) or (not(w) and z and y and not(x)) or (not(w) and z and y and x):
                        print(x, y, z, w)

def task_5():
    for n in range(1, 1000000):
        n2 = bin(n)[2:]
        
        zero = n2.count('0')
        one = n2.count('1')

        p = f'{one:b}' + f'{zero:b}'
        
        r = int(p, 2)

        if r == 183:
            print(n)
            break

def task_6():
    screensize(2000, 2000)

    pendown()

    k = 100

    begin_fill()
    for i in range(2):
        forward(12 * k)
        right(150)
        forward(12 * k)
        right(30)
    end_fill()

    canvas = getcanvas()

    cnt = 0
    for x in range(-500, 500):
        for y in range(-500, 500):
            if canvas.find_overlapping(x * k, y * k, x * k, y * k) == (5,):
                cnt += 1

    print(cnt)

def task_8():
    alph = 'АВОРТ'
    cnt = 0

    for i in product(alph, repeat=4):
        wd = ''.join(i)
        cnt += 1

        if wd == 'ВАТА':
            print(cnt)

def task_9():
    with open('24.04.2026/9.txt', 'r') as f:
        count = 0

        for line in f:
            nums = list(map(int, line.split()))

            ch = [i for i in nums if i % 2 == 0]
            nch = [i for i in nums if i % 2 != 0]

            if len(nums) == len(set(nums)):
                if len(nch) > len(ch):
                    if sum(nch) < sum(ch):
                        count += 1

    print(count)

def task_12():
    for p in range(12, 100):
        for x in range(p):
            for y in range(p):
                for z in range(p):
                    a = z * p ** 1 + x * p ** 0
                    b = x * p ** 1 + y * p ** 0
                    c = z * p ** 2 + y * p ** 1 + 11 * p ** 0

                    if (a + b) == c:
                        result = x * p ** 2 + y * p ** 1 + z * p ** 0

                        return result

def task_13():
    for A in range(1000):
        f = True

        for x in range(1000):
            if not(not(x & 29 != 0) or (not(x & 17 == 0) or (x & A != 0))):
                f = False
                break
        
        if f:
            print(A)
            break


# task_2()
# task_5()
# task_6()
# task_8()
# task_9()
# print(task_12())
# task_13()