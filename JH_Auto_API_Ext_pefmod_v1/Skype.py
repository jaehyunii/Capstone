import pefile
pe = pefile.PE('C:/Program Files (x86)/Microsoft/Skype for Desktop/Skype.exe')
pe
pe.parse_data_directories()

file = open("SkypeAPI.txt",'w')
pe.parse_data_directories()

for entry in pe.DIRECTORY_ENTRY_IMPORT:
     for imp in entry.imports:
        file.write("'"+str(imp.name).replace("b'","")+",")
file.close()

f=open("SkypeAPI.txt","r")
data=f.readlines()
data_t=[]
for i in data:
    data_t.append(i[:-1])
f.close()

import pandas as pd
f1=pd.read_csv("SkypeAPI.txt",delimiter=',')
f1=f1.transpose()
f1.to_csv("./SkypeAPI.csv")