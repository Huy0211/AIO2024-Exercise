# Câu 3:

import random
import math

# Hàm tính MAE


def calc_mae(n):
    print('Loss name = MAE')
    mae = 0
    final_mae = 0
    for i in range(n):
        print(f'samples: {i}')
        y = random.uniform(0, 10)
        y_hat = random.uniform(0, 10)
        print(f"y = {y} | y_hat = {y_hat}")
        abs_error = abs(y-y_hat)
        mae = mae + abs_error
        mae = mae/n
        final_mae = final_mae + mae
        print(f'Loss: {mae}')
    print(f'Final MAE: {final_mae}')

# Hàm tính MSE


def calc_mse(n):
    print('Loss name = MSE')
    mse = 0
    final_mse = 0
    for i in range(n):
        print(f'samples: {i}')
        y = random.uniform(0, 10)
        y_hat = random.uniform(0, 10)
        print(f"pred = {y} | target = {y_hat}")
        abs_error = (y-y_hat)**2
        mse = mse + abs_error
        mse = mse/n
        final_mse = final_mse + mse
        print(f'Loss: {mse}')
    print(f'Final MSE: {final_mse}')

# Hàm tính RMSE


def calc_rmse(n):
    print('Loss name = RMSE')
    rmse = 0
    final_rmse = 0
    for i in range(n):
        print(f'samples: {i}')
        y = random.uniform(0, 10)
        y_hat = random.uniform(0, 10)
        print(f"pred = {y} | target = {y_hat}")
        abs_error = (y-y_hat)**2
        rmse = rmse + abs_error
        rmse = math.sqrt(rmse/n)
        final_rmse = final_rmse + rmse
        print(f'Loss: {rmse}')
    print(f'Final RMSE: {final_rmse}')


if __name__ == '__main__':
    n = input('Input number of samples (integer number):')
    if n.isnumeric():
        n = int(n)
        loss_name = input('Input loss name (mae|mse|rmse):')
        if loss_name == 'mae':
            print(calc_mae(n))
        elif loss_name == 'mse':
            print(calc_mse(n))
        elif loss_name == 'rmse':
            print(calc_rmse(n))
    else:
        print('Number of samples must be an integer number')
