import os
import numpy as np

path = []
# 此py文件和数据文件夹在同一目录下
for root, dirs, files in os.walk('./data'):
    for file in files:
        realpath = os.path.join(root, file)
        path.append(realpath)

data = np.zeros((len(path),200))

# 这里由于需要根据文件名对文件进行排序，因此文件名中的序号应该为两位，比如S_u1,应该为S_u01
# 这里的[10:12]是排序的依据， 根据path的值推算而出，比如说path的其中一项为”./data/S_u00.txt“， 那么它的[10, 12]是00
# 你在运行的时候可以输出一个path的值看一下，看[10,12]是否需要修改
for i, p in enumerate(sorted(path, key=lambda x: int(x[10:12]))):
    # print(i)
    # print(p)
    with open(p, errors='ignore') as f:
        c = 0
        for line in f.readlines():
            data[i][c] = float(line.replace('\n', ''))
            c += 1

np.savetxt("result.csv", data.T, delimiter=",")
