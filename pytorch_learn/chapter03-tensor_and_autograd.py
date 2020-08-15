# -*- coding: utf-8 -*

import torch
import numpy as np

x = torch.ones(1)
b = torch.randn(1, requires_grad=True)
w = torch.randn(1, requires_grad=True)

y = w * x
z = y + b
print(x.requires_grad, b.requires_grad, w.requires_grad)

#这个有点难懂，以后再详细看看.