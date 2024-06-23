import torch
import torch.nn as nn


class Softmax(nn.Module):
    def __init__(self) -> None:
        super().__init__()

    def forward(self, x):
        softmax_x = torch.exp(x) / sum(torch.exp(x))
        return softmax_x


class softmax_stable(nn.Module):
    def __init__(self) -> None:
        super().__init__()

    def forward(self, x):
        softmax_stable_x = torch.exp(x - torch.max(x)) / sum(
            torch.exp(x - torch.max(x))
        )
        return softmax_stable_x


# Testcases:
if __name__ == "__main__":
    data = torch.tensor([1, 2, 3])
    softmax = Softmax()
    output_1 = softmax(data)
    print(output_1)
    softmax_stable = softmax_stable()
    output_2 = softmax_stable(data)
    print(output_2)
