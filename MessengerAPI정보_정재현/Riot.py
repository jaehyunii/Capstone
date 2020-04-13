import pefile
pe = pefile.PE('C:/Users/User/AppData/Local/riot-web/Riot.exe')
pe
pe.parse_data_directories()

file = open("RiotAPI.txt",'w')
pe.parse_data_directories()

for entry in pe.DIRECTORY_ENTRY_IMPORT:
     for imp in entry.imports:
        file.write("'"+str(imp.name).replace("b'","")+",")
file.close()

f=open("RiotAPI.txt","r")
data=f.readlines()
data_t=[]
for i in data:
    data_t.append(i[:-1])
f.close()

import pandas as pd
f1=pd.read_csv("RiotAPI.txt",delimiter=',')
f1=f1.transpose()
f1.to_csv("./RiotAPI.csv")