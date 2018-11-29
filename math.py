import random

def add_f():
    a = random.randint(0, 9)
    # print a
    b = random.randint(0, 10-a)
    print '%d + %d = ' % (a, b)

def sub_f():
    a = random.randint(0, 9)
    b = random.randint(0, a)
    print '%d - %d = ' % (a, b)

if __name__ == '__main__':
    for i in range(0, 100):
        c = random.randint(0, 1)
        if (c == 1):
            add_f()
        else:
            sub_f()