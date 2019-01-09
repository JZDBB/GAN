import h5py
import numpy as np

# h5格式读取
def read_data(filename):
    with h5py.File(filename,'r') as f:

        def print_name(name):
            print(name)
        f.visit(print_name)
        for key in f.keys():
            print(f[key].name)
            print(f[key].dtype)
            print(f[key].shape)
            print(f[key].size)
            data = f[key]
            print(data[:])

read_data('./cub/text_c10/001.Black_footed_Albatross/Black_Footed_Albatross_0001_796111.h5')
