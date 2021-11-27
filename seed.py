import torch
import numpy as np
import random

SEED = 1
torch.manual_seed(SEED)
torch.cuda.manual_seed_all(SEED)
np.random.seed(SEED)
random.seed(SEED)

class print_random:
    def print_float(self):
        print(random.random())
        print(torch.rand(3))
        print(np.random.random(3))


print('seed')
P = print_random()
P.print_float()