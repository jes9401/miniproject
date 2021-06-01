import glob
import csv
import pandas as pd

path1 = '.\\*2018년.csv'
path2 = '.\\*2019년.csv'
path3 = '.\\*2020년.csv'
merge_path = './merge.csv'
file_list = []
file_list.extend(glob.glob(path1))
file_list.extend(glob.glob(path2))
file_list.extend(glob.glob(path3))

with open(merge_path,'w') as f:
        for i,file in enumerate(file_list):
                if i==0:
                        with open(file,'r') as f2:
                                while True:
                                        line = f2.readline()
                                        if not line:
                                                break
                                        f.write(line)
                else:
                        with open(file,'r') as f2:
                                n = 0
                                while True:
                                        line = f2.readline()
                                        if n != 0:
                                                f.write(line)
                                        if not line:
                                                break
                                        n+=1

df = pd.read_csv(merge_path)
df.to_csv(os.path.join(merge_path), encoding='utf-8', index=False)
