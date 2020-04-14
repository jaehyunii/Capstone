import pefile
import pandas as pd

path = input("시작하려면 start입력")

while path != "q":
    path = input("주소입력 / 끝내기 : [q] 입력")
    if path == "q":
        break
    pe = pefile.PE(path)

    file = open("APIList.txt", 'w')

    pe.parse_data_directories()


    file.write("api" + "\n")
    for entry in pe.DIRECTORY_ENTRY_IMPORT:
        file.write("'" + str(entry.dll)[2:] + "\n")
        for imp in entry.imports:
            file.write("'" + str(imp.name)[2:] + "\n")

    file.close()

    f1 = pd.read_csv('APIList.txt', delimiter='\t')
    # f1.to_csv("C:\\Users\\br179\\PycharmProjects\\capstone\\APItest2.csv")
    csv1 = pd.read_csv("C:\\Users\\br179\\PycharmProjects\\capstone\\APItest2.csv")
    csv1.drop(csv1.columns[0:1], axis='columns')

    finalcsv = pd.concat([csv1, f1], axis=1)
    finalcsv = finalcsv.drop(finalcsv.columns[0:1], axis='columns')
    finalcsv.to_csv("C:\\Users\\br179\\PycharmProjects\\capstone\\APItest2.csv")

print("end")