from types import new_class
import torch 
import numpy as np
from collections import OrderedDict


def rm_substr_from_state_dict(state_dict, substr):
    new_state_dict = OrderedDict()
    for key in state_dict.keys():
        if substr in key:  # to delete prefix 'module.' if it exists
            new_key = key[len(substr):]
            new_state_dict[new_key] = state_dict[key]
        else:
            new_state_dict[key] = state_dict[key]
    return new_state_dict

def add_substr_from_state_dict(state_dict, substr1, substr2):
    new_state_dict = OrderedDict()
    for key in state_dict.keys():
        new_key = substr1 + key if key[:2]!='fc' else substr2 + key
        new_state_dict[new_key] = state_dict[key]
    return new_state_dict

def add_key(path, key, value, saved_path):
    model = torch.load(path)
    del model['CLASSES']
    del model['epoch']
    model[key] = value
    print(model.keys())
    torch.save(model, saved_path)

def reset_model(path, saved_path):
    model = torch.load(path)
    print(model.keys())
    new_state = add_substr_from_state_dict(model, 'backbone.', 'head.')
    print(len(new_state), new_state.keys())
    model['state_dict'] = new_state
    torch.save(model, saved_path)



def main():
    # path = 'tent/ckpt/cifar10/corruptions/Standard.pt'
    # reset_model(path)
    
    # model = torch.load('/home/dqwang/code/mmclassification/work_dirs/tent_resnet18_b256_cifar102/epoch_1.pth')
    # print(model.keys())
    # print(model['meta']['CLASSES'])

    path = '/home/dqwang/jingao/mmcls/work_dirs/resnet/resnet50-0676ba61.pth'
    saved_path = '/home/dqwang/jingao/mmcls/work_dirs/resnet/resnet50.pth'
    # value = OrderedDict({'epoch':100, 'CLASSES': ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']})
    # add_key(path, 'meta', value)
    reset_model(path, saved_path)


if __name__=='__main__':
    main()
