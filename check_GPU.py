import pynvml
pynvml.nvmlInit()
# 这里的1是GPU id
handle = pynvml.nvmlDeviceGetHandleByIndex(1)
meminfo = pynvml.nvmlDeviceGetMemoryInfo(handle)
print(meminfo.used/1024/1024, 'M')#这里是字节bytes，所以要想得到以兆M为单位就需要除以1024**2