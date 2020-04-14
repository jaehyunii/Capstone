import pefile
exe = pefile.PE('C:/Program Files (x86)/exefiles/ZapyaPC2706Lite.exe')

file = open("ZapyaPCAPI.txt", 'w')
exe.parse_data_directories()

for entry in exe.DIRECTORY_ENTRY_IMPORT:
    for imp in entry.imports:
        file.write("'"+str(imp.name).replace("b'","")+",")

file.close()

f=open("ZapyaPCAPI.txt", 'r')

data=f.readlines()
data_t=[]

for i in data:
    data_t.append(i[:-1])

f.close()

import pandas as pd
f1=pd.read_csv('ZapyaPCAPI.txt', delimiter=',')

f1=f1.transpose()
f1.to_csv("./ZapyaPCAPI.csv")