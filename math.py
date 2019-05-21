import random
from gen_doc import Exam

class Expression():
    (ADD, SUB, ADD_SUB, MUL, DIV, MUL_DIV) = range(0, 6)
    (CARRY, CARRY_NOT, CARRY_ALL) = range(0, 3)

    def __init__(self, num=0):
        self.exp = {}
        self.num = num
        self.a_max = 100
        self.a_min = 0
        self.b_max = 100
        self.b_min = 0

        self.carry = self.CARRY_ALL

    def generate(self, type=ADD_SUB):
        while len(self.exp.keys()) < self.num:
            if self.ADD_SUB == type:
                type = random.randint(self.ADD, self.SUB)

            if self.ADD == type:
                exp = self.add(self.a_min, self.a_max, self.b_min, self.b_max)
            elif self.SUB == type:
                exp = self.sub(self.a_min, self.a_max, self.b_min, self.b_max)

            self.exp[exp] = 1

    def add(self, a_min=0, a_max=0, b_min=0, b_max=0):
        while True:
            a = self.gen_num(a_min, a_max)
            b = self.gen_num(b_min, b_max)
            if self.CARRY_NOT == self.carry:
                if ((a % 10) + (b % 10)) >= 10:
                    continue # re-gen

            if self.CARRY == self.carry:
                if ((a % 10) + (b % 10)) < 10:
                    continue # re-gen

            if (a + b) >= 100:
                continue # re-gen

            return '%d + %d = ' % (a, b)

    def sub(self, a_min=0, a_max=0, b_min=0, b_max=0):
        while True:
            a = self.gen_num(a_min, a_max)
            b = self.gen_num(b_min, b_max)

            if a < b:
                continue  # re-gen

            if self.CARRY_NOT == self.carry:
                if ((a % 10) < (b % 10)):
                    continue  # re-gen

            if self.CARRY == self.carry:
                if ((a % 10) >= (b % 10)):
                    continue  # re-gen

            return '%d - %d = ' % (a, b)

    def gen_num(self, min=0, max=1):
        return random.randint(min, max)

if __name__ == '__main__':
    e = Expression()
    e.num = 100

    e.a_min = 10
    e.a_max = 99
    e.b_min = 1
    e.b_max = 9
    e.carry = Expression.CARRY

    for pages in range(10):
        e.generate(Expression.SUB)

        ex = Exam()

        for i, key in enumerate(e.exp.keys()):
            print ('%d, %s' % (i, key))
            ex.add(i, key)

        ex.format_sheet(1, 27)
        ex.save('sample_%d.xlsx' % pages)
