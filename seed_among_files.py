import torch
import numpy as np
import random

SEED = 1
torch.manual_seed(SEED)
torch.cuda.manual_seed_all(SEED)
np.random.seed(SEED)
random.seed(SEED)

from seed import print_random

print('other')
P = print_random()
P.print_float()