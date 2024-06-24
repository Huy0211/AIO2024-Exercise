import torch
import torch.nn as nn


class MySoftmax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        x_exp = torch.exp(x)
        sum_exp = x_exp.sum(0, keepdim=True)
        return x_exp / sum_exp


class StableSoftmax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        c = torch.max(x, dim=0)
        x_exp = torch.exp(x - c.values)
        sum_exp = x_exp.sum(0, keepdim=True)
        return x_exp / sum_exp


data = torch.Tensor([1, 2, 3])
my_softmax = MySoftmax()
output = my_softmax(data)
print(output)
