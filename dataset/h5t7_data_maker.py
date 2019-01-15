import h5py
import numpy as np
import os


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
    return 0
# read_data('./cub/text_c10/001.Black_footed_Albatross/Black_Footed_Albatross_0001_796111.h5')
# read_data('Data/faces/texth5/1.h5')

# h5格式写入
def write_data(data_dir, h5_dir):
    filenames = os.listdir(data_dir)
    for filename in filenames:
        name = filename.split('.')[0] + '.h5'
        h5_file = os.path.join(h5_dir, name)
        with h5py.File(h5_file, 'w') as f:
            filename = os.path.join(data_dir, filename)
            try:
                file = open(filename, 'r').read()
            except:
                file = open(filename, 'r', encoding='utf-8').read()
            lines = file.split('\n')
            for i in range(5):
                key = 'txt%d' %i
                list_mesg = list(lines[i])
                mesgs = []
                for mesg in list_mesg:
                    mesgs.append(ord(mesg))
                mesgs = np.array(mesgs, dtype='float64')
                f[key] = mesgs
            f.close()
write_data('Data/faces/text', 'Data/faces/texth5')


