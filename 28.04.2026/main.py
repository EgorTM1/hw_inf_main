from turtle import *
from itertools import product


def task_2():
    print('x y z w')

    for x in range(2):
        for y in range(2):
            for z in range(2):
                for w in range(2):
                    if (not(x) and z and not(y) and not(w)) or (not(x) and z and y and not(w)) or (not(x) and z and y and w):
                        print(x, y, z, w)


def task_5():
    for n in range(1, 1000):
        n2 = bin(n)[2:]

        if n % 5 == 0:
            n2 += '11'
        if n % 5 != 0:
            n2 += bin(n // 5)[2:]
        
        r = int(n2, 2)

        if r >= 783 and n % 2 != 0:
            print(n)
            break
        

def task_6():
    screensize(2000, 2000)

    pendown()

    k = 100

    begin_fill()
    for i in range(2):
        forward(15 * k)
        right(90)
        forward(23 * k)
        right(90)
    end_fill()

    penup()

    forward(3 * k)
    right(90)
    forward(5 * k)
    left(90)

    pendown()

    begin_fill()
    for i in range(2):
        forward(252 * k)
        right(90)
        forward(398 * k)
        right(90)
    end_fill()
    

    canvas = getcanvas()

    count = 0
    for x in range(-1000, 1000):
        for y in range(-1000, 1000):
            if canvas.find_overlapping(x * k, y * k, x * k, y * k) != ():
                count += 1

    
    print(count)


def task_7():
    for i in range(1, 1_000_000):
        I = 4 * 33000 * 37 * 2493 + i * 1024 * 8 * 30

        t = I / 363_956_352

        if t > 307:
            print(i)
            break


def task_8():
    alph = '0123456789ABCDE'
    count = 0

    for i in product(alph, repeat=4):
        if i[0] != '0' and i.count('8') == 1:
            f = True

            for j in range(1, len(i)):
                if i[j] == i[j - 1]:
                    f = False
                    break

            if f:
                count += 1

    print(count)


def task_9():
    with open('28.04.2026/9.txt', 'r') as file:
        count = 0

        for line in file:
            nums = sorted(map(int, line.split()))
            np = sorted([i for i in nums if nums.count(i) == 1])

            if (nums.count(nums[0]) == 2 and len(np) == 6) or (nums.count(nums[0]) == 3 and len(np) == 5):
                if np[0] ** 2 + np[-1] ** 2 <= sum(np[1:-1]) ** 2:
                    count += 1

    
    print(count)


def task_14():
    res = 0

    for x in range(1, 8411):
        a = 29 ** 293 + 29 ** 271 - x
        count = 0

        while a > 0:
            if a % 29 == 0:
                count += 1

            a //= 29

        res = max(count, res)
    
    print(res)

def task_15():
    for A in range(1000, 0, -1):
        f = True

        for x in range(1, 1000):
            for y in range(1, 1000):
                if not((y > A) or (152 != 2 * y + 3 * x) or (A < x)):
                    f = False
                    break

            if not(f):
                break

        if f:
            print(A)
            break



task_2()
task_5()
# task_6()
task_7()
task_8()
task_9()
task_14()
task_15()
