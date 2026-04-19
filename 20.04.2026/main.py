def task_1():
    cnt = 0

    for G in range(-1000, 1000):
        flag = True

        for f in range(0, 1000):
            for h in range(0, 1000):
                if not((not(f < G) or (f ** 2 < 81)) and (not(h ** 2 <= 36) or (h <= G))):
                    flag = False
                    break

            if not(flag):
                break

        if flag:
            cnt += 1

    print(cnt)

def task_2():
    lst = []

    for G in range(0, 10000):
        flag = True

        for f in range(0, 1000):
            for h in range(0, 1000):
                if not((f >= G) or (h >= G) or (f * h <= 205)):
                    flag = False
                    break

            if not(flag):
                break

        if flag:
            lst.append(G)

    print(max(lst))

def task_3():
    cnt = 0

    for G in range(-1000, 1000):
        flag = True

        for f in range(0, 1000):
            for h in range(0, 1000):
                if not((not(f < 6) or (f ** 2 < G)) and (not(h ** 2 <= G) or (h <= 6))):
                    flag = False
                    break

            if not(flag):
                break

        if flag:
            cnt += 1

    print(cnt)

def task_4():
    maxx = -1

    for G in range(0, 10000):
        flag = True

        for f in range(0, 1000):
            for h in range(0, 1000):
                if not((h + 2 * f != 48) or (G < f) or (f < h)):
                    flag = False
                    break

            if not(flag):
                break

        if flag:
            maxx = max(maxx, G)

    print(maxx)

def task_5():
    for G in range(0, 1000):
        flag = True

        for f in range(0, 1000):
            for h in range(0, 1000):
                if not(not(f < 9) or (not(5 * h < f) or (2 * f * h < G))):
                    flag = False
                    break

            if not(flag):
                break

        if flag:
            print(G)
            break

def task_6():
    for G in range(0, 1000):
        flag = True

        for f in range(0, 1000):
            for h in range(0, 1000):
                if not((f < G) or (h < G) or (h < f - 5) or (h < 2 * f - 15)):
                    flag = False
                    break

            if not(flag):
                break

        if flag:
            print(G)
            break

def task_7():
    maxx = -1

    for G in range(0, 10000):
        flag = True

        for f in range(0, 1000):
            for h in range(0, 1000):
                if not((h + 2 * f > G) or (f < 13) or (h < 44)):
                    flag = False
                    break

            if not(flag):
                break

        if flag:
            maxx = max(maxx, G)

    print(maxx)

def task_8():
    for G in range(0, 1000):
        flag = True

        for f in range(0, 1000):
            for h in range(0, 1000):
                if not((f + 2 * h < G) or (h < f) or (h > 22)):
                    flag = False
                    break

            if not(flag):
                break

        if flag:
            print(G)
            break

def task_9():
    for G in range(0, 1000):
        flag = True

        for f in range(0, 1000):
            for h in range(0, 1000):
                if not((f >= 12) or (3 * f < h) or (f * h < G)):
                    flag = False
                    break

            if not(flag):
                break

        if flag:
            print(G)
            break

def task_10():
    maxx = -1

    for G in range(0, 10000):
        flag = True

        for f in range(0, 1000):
            for h in range(0, 1000):
                if not((2 * f + h != 70) or (f < h) or (G < f)):
                    flag = False
                    break

            if not(flag):
                break

        if flag:
            maxx = max(maxx, G)

    print(maxx)


task_1()
task_2()
task_3()
task_4()
task_5()
task_6()
task_7()
task_8()
task_9()
task_10()

# 4
# 15
# 23
# 15
# 17
# 508
# 69
# 67
# 364
# 23