import os

path = '/home/dqwang/datasets/imagenet-c/brightness/1'  # 50,000
path = '/home/dqwang/datasets/imagenet/val'  # 50,000
path = '/home/dqwang/datasets/imagenet/train'  # 1,281,167
def walkFile(file):
    count = 0
    for root, dirs, files in os.walk(file): 
        for f in files:
            count += 1
    print(file, 'has', count, 'files')
walkFile(path)