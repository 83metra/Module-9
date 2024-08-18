def is_prime(func):
    def wrapper(*args):
        n = func(*args)
        if n <= 1:
            return f'Простое\n{n}'
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return f'Составное\n{n}'
            else:
                return f'Простое\n{n}'
    return wrapper

@is_prime
def sum_three(*args):
    return sum(args)

result = sum_three(2, 3, 6)
print(result)

result = sum_three(1, 3, 8, 6, 8)
print(result)

result = sum_three(100,1)
print(result)
