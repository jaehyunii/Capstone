import pefile
import pandas as pd
import os

a= []
a1 = pd.DataFrame(a)
a1.to_csv("C:\\Users\\br179\\PycharmProjects\\capstone\\APItest3.csv")  # 저장할 csv파일 생성

path1212 = r'C:\Users\br179\Desktop\exe' # exe파일 저장한 경로
file_list = os.listdir(path1212)
file_list.append('q')

path = input("시작하려면 start입력")

while path != "q":
    for i in file_list:
        path = path1212+"\\"+i
        if path == path1212+"\\"+file_list[-1]:
            break
        pe = pefile.PE(path)

        file = open("APIList3.txt", 'w')

        pe.parse_data_directories()


        file.write("api" + "\n")
        for entry in pe.DIRECTORY_ENTRY_IMPORT:
            file.write("'" + str(entry.dll)[2:] + "\n")
            for imp in entry.imports:
                file.write("'" + str(imp.name)[2:] + "\n")

        file.close()

        f1 = pd.read_csv('APIList3.txt', delimiter='\t')
        csv1 = pd.read_csv("C:\\Users\\br179\\PycharmProjects\\capstone\\APItest3.csv")
        csv1.drop(csv1.columns[0:1], axis='columns')

        finalcsv = pd.concat([csv1, f1], axis=1)
        finalcsv = finalcsv.drop(finalcsv.columns[0:1], axis='columns')
        finalcsv.to_csv("C:\\Users\\br179\\PycharmProjects\\capstone\\APItest3.csv")
    break

print("end")
