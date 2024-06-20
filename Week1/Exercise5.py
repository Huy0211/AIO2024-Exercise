# Câu 5:

def md_nre_single_sample(y, y_hat, n, p):
    y_root = y**(1/n)
    y_hat_root = y_hat**(1/n)
    difference = y_root - y_hat_root
    loss = difference**p
    return loss


if __name__ == '__main__':
    print(md_nre_single_sample(100, 99.5, 2, 1))
    print(md_nre_single_sample(50, 49.5, 2, 1))
    print(md_nre_single_sample(20, 19.5, 2, 1))
    print(md_nre_single_sample(0.6, 0.1, 2, 1))
