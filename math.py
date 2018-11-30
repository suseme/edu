import random

def add_f(min, max):
    a = random.randint(0, max-1)
    # print a
    b = random.randint(0, max-a)
    return '%d + %d = ' % (a, b)

def sub_f(min, max):
    a = random.randint(0, max-1)
    b = random.randint(0, a)
    return '%d - %d = ' % (a, b)

if __name__ == '__main__':
    num = 100
    max = 10
    fms = {}

    while len(fms.keys()) < num:
        c = random.randint(0, 1)
        if (c == 1):
            fm = add_f(0, max)
        else:
            fm = sub_f(0, max)
        fms[fm] = 1

    no = 1
    for key in fms.keys():
        print ('%03d. %s' % (no, key))
        no += 1
