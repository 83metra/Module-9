class StepValueError(ValueError):
    pass

class IteratoError():
    pass

class Iterator:
    def __init__(self, start, stop, step = 1):
        self.start, self.stop, self.step = start - step, stop, step
        if self.step == 0:
            raise StepValueError()
    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        if self.step < 0:
            self.pointer += self.step
            while self.stop > self.pointer:
                raise StopIteration
            return self.pointer
        if self.step > 0:
            self.pointer += self.step
            while self.stop < self.pointer:
                raise StopIteration
            return self.pointer

    def say_info(self):
        print(self.start, self.stop, self.step, self.pointer)


try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print()

