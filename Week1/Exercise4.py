# Câu 4:

# Hàm tính giai thừa
def factorial_func(a):
    if a < 0:
        raise ValueError('MathError!')
    elif a == 0:
        return 1
    else:
        giai_thua = 1
        for i in range(1, a+1):
            giai_thua *= i
        return giai_thua

# Hàm tính sin


def sin_func(x, n):
    total = 0
    for i in range(0, n+1):
        total = total + ((-1)**i)*(x**(2*i+1))/(factorial_func((2*i)+1))
    print(f'sin({x}) = {total}')

# Hàm tính cos


def cos_func(x, n):
    total = 0
    for i in range(0, n+1):
        total = total + ((-1)**i)*(x**(2*i))/factorial_func(2*i)
    return total

# Hàm tính sinh


def sinh_func(x, n):
    total = 0
    for i in range(0, n+1):
        total = total + (x**(2*i+1))/(factorial_func((2*i)+1))
    print(f'sinh({x}) = {total}')

# Hàm tính cosh


def cosh_func(x, n):
    total = 0
    for i in range(0, n+1):
        total = total + (x**(2*i))/factorial_func(2*i)
    print(f'cosh({x}) = {total}')


if __name__ == '__main__':
    sin_func(x=3.14, n=10)
    print(round(cos_func(x=3.14, n=10), 2))
    sinh_func(x=3.14, n=10)
    cosh_func(x=3.14, n=10)
