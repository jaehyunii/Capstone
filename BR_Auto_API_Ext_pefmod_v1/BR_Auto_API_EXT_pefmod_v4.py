import pefile
import pandas as pd
import os
import sys

a= [] #csv파일을 만들기위한 dataFrame형식을 만들기위해 빈 배열 생성
j=0
a1 = pd.DataFrame(a) #dataFrame 생성
a1.to_csv("C:\\Users\\br179\\api\\APItest3.csv")  # 저장할 csv파일 생성
a1.to_csv("C:\\Users\\br179\\api\\API_total.csv")  # 저장할 csv파일 생성

path1 = r'C:\Users\br179\exe' # 실제 exe 파일 저장장소
path_name = r'C:\Users\br179\exe_name' # exe파일 이름을 대조시키기위한 폴더
file_list2 = os.listdir(path_name)  # 파일경로에대한 모든파일을 도출
file_list3 = os.listdir(path1)
file_list = [file for file in file_list2 if file.endswith(".exe")] # exe파일 이름만 도출하기위한 코드

if(len(file_list) != len(file_list3)):  # exe_name 폴더에 잘 옮겻나 확인하기위한 코드
    print("exe폴더와 exe_name폴더의 파일 갯수가 다릅니다.")
    sys.exit()

path_res = [] # path 저장소
for root, dirs, files in os.walk(path1):
    rootpath = os.path.join(os.path.abspath(path1),root) # join : 병합 // abspath : 절대 경로
    for file in files:
        if(file.endswith(".exe")):
            for i in file_list:
                if(file == i):
                    filepath = os.path.join(rootpath, file)
                    path_res.append(filepath)

# path_res 예시
# C:\Users\br179\exe\Sonma Typing-Expert\Sonma Typing-Expert.exe
# C:\Users\br179\exe\TypingMaster10\tmaster.exe
# C:\Users\br179\exe\WinRAR\WinRAR.exe
# ...

for i in path_res: # 변수 i에 file_list에 있는 string을 불러온다 , 이때 폴더설정에서 파일에 대한 확장자가 표기되어야함 없을시에는 .exe를 붙여줘야함

    path = i # path_res list의 원소들을 path로 설정

    pe = pefile.PE(path)                    # pefile경로를 각파일에대한 경로로 설정

    file = open("C:\\Users\\br179\\api\\txt\\"+file_list[j][:-4]+".txt", 'w') # API_name.txt를 생성

    pe.parse_data_directories()

    file.write( file_list[j][:-4] + "\n")  #각 열에대한 exe파일이름을 추가하여 열 구분, i[:-4]는 .exe를 빼고 이름을 넣기위함 ex) kakao.exe -> kakao
    for entry in pe.DIRECTORY_ENTRY_IMPORT:  # txt파일에 api목록들을 넣음 // dataframe을 쉽게 나누기위해 줄바꿈단위로 입력함
        # file.write("'" + str(entry.dll)[2:] + "\n")
        for imp in entry.imports:
            if str(imp.name) != 'None':
                file.write("'" + str(imp.name)[2:] + "\n")

    file.close()

    f1 = pd.read_csv("C:\\Users\\br179\\api\\txt\\"+file_list[j][:-4]+".txt", delimiter='\t')  # APIList3.txt를 줄바꿈단위로 pandas로 csv를 읽음

    f2 = f1[file_list[j][:-4]].value_counts() # 중복된 api 횟수를 count하기 위한 함수 -> dataframe이 아닌 series형태
    df1 = pd.DataFrame(data=f2.index, columns=['api name'])
    df2 = pd.DataFrame(data=f2.values, columns=['counter'])
    df = pd.merge(df1, df2, left_index=True, right_index=True) # Series를 dataframe type으로 바꿔줌
    df.to_csv("C:\\Users\\br179\\api\\counter\\"+file_list[j][:-4]+"_count.csv")

    f1.duplicated()
    f1 = f1.drop_duplicates() # datatframe에서 중복된 값 처리
    f3 = pd.DataFrame({'program name': [file_list[j][:-4]], "api amount" : [len(f1)]}) # 프로그램별 api 갯수
    csv1 = pd.read_csv("C:\\Users\\br179\\api\\APItest3.csv") #처음에 생성한 빈 파일을 csv로 불러옴, 저장되잇던 csv파일 불러옴
    csv1.drop(csv1.columns[0:1], axis='columns') # 첫번째 열 제거 (열번호가 적혀서 출력되어 병합할때 문제가 생김)
    csv2 = pd.read_csv("C:\\Users\\br179\\api\\API_total.csv")
    csv2.drop(csv1.columns[0:1], axis='columns')

    finalcsv = pd.concat([csv1, f1], axis=1) # 두 csv를 병합
    finalcsv = finalcsv.drop(finalcsv.columns[0:1], axis='columns')  # 첫번째 열 제거
    finalcsv2 = pd.concat([csv2, f3])  # 두 csv를 병합
    finalcsv2 = finalcsv2.drop(finalcsv2.columns[0:1], axis='columns')  # 첫번째 열 제거
    finalcsv.to_csv("C:\\Users\\br179\\api\\APItest3.csv") # 최종적으로 저장
    finalcsv2.to_csv("C:\\Users\\br179\\api\\API_total.csv")  # 최종적으로 저장
    j=j+1

print("----------")
print(" complete ")
print("----------")


