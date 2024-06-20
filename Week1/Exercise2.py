# Câu 2:

import math
# Hàm Sigmoid


def sigmoid_function(x):
    print(f'Sigmoid: f(x) = {1/(1+math.exp(-x))}')

# Hàm ReLU


def relu_function(x):
    if x <= 0:
        print(f'ReLU: f(x) = {0}')
    else:
        print(f'ReLU: f(x) = {x}')

# Hàm ELU


def elu_function(x):
    alpha = 0.01
    if x <= 0:
        print(f'ELU: f(x) = {alpha*(math.exp(x)-1)}')
    else:
        print(f'ELU: f(x) = {x}')

# Hàm kiểm tra x có hợp lệ không


def is_number(x):
    try:
        float(x)
    except ValueError:
        return False
    return True

# Hàm kiểm tra activation function name có hợp lệ hay không


def exercise2(x, ten_function_user):
    if ten_function_user == "sigmoid":
        return sigmoid_function(x)
    elif ten_function_user == "relu":
        return relu_function(x)
    elif ten_function_user == "elu":
        return elu_function(x)
    else:
        print(f'{ten_function_user} is not supported')


if __name__ == '__main__':
    x = input('Input x: ')
    # Kiểm tra x có hợp lệ hay không (Nếu hợp lệ chuyển x sang float type)
    if is_number(x):
        x = float(x)
        # Kiểm tra activation function name có hợp lệ hay không
        ten_function_user = input(
            'Input Activation Function(sigmoid|relu|elu): ')
        exercise2(x, ten_function_user)
    else:
        print('x must be a number')  # (Nếu không hợp lệ thì thông báo)
