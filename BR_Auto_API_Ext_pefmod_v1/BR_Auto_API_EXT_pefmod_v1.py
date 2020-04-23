import pefile
import pandas as pd
import os

a= [] #csv파일을 만들기위한 dataFrame형식을 만들기위해 빈 배열 생성
a1 = pd.DataFrame(a) #dataFrame 생성
a1.to_csv("C:\\Users\\br179\\PycharmProjects\\capstone\\APItest3.csv")  # 저장할 csv파일 생성

path1212 = r'C:\Users\br179\Desktop\exe' # exe파일 저장한 경로
file_list2 = os.listdir(path1212)  # 파일경로에대한 모든파일을 도출
file_list = [file for file in file_list2 if file.endswith(".exe")] #exe파일만 도출하기위한 코드
file_list.append('q') #마지막에 반복문을 마무리하기위한 'q'를 append 한다

path = input("시작하려면 start입력 or 끝내려면 q")

while path != "q": # 'q'입력시 반복문 종료
    for i in file_list: # 변수 i에 file_list에 있는 string을 불러온다
        path = path1212+"\\"+i # 각 파일의 이름과 exe파일들을 저장한경로를 붙여 파일들에대한 최종경로를 생성
        if path == path1212+"\\"+file_list[-1]: # 마지막 파일에대한 반복문이 끝났을때
            break                               #  반복문 종료

        pe = pefile.PE(path)                    # pefile경로를 각파일에대한 경로로 설정

        file = open("APIList3.txt", 'w') # APIList3.txt를 생성

        pe.parse_data_directories()

        file.write( i + "\n")  #각 열에대한 exe파일이름을 추가하여 열 구분
        for entry in pe.DIRECTORY_ENTRY_IMPORT:  # txt파일에 api목록들을 넣음 // dataframe을 쉽게 나누기위해 줄바꿈단위로 입력함
            file.write("'" + str(entry.dll)[2:] + "\n")
            for imp in entry.imports:
                file.write("'" + str(imp.name)[2:] + "\n")

        file.close()

        f1 = pd.read_csv('APIList3.txt', delimiter='\t')  # APIList3.txt를 줄바꿈단위로 pandas로 csv를 읽음
        csv1 = pd.read_csv("C:\\Users\\br179\\PycharmProjects\\capstone\\APItest3.csv") #처음에 생성한 빈 파일을 csv로 불러옴
        csv1.drop(csv1.columns[0:1], axis='columns') # 첫번째 열 제거 (열번호가 적혀서 출력되어 병합할때 문제가 생김)

        finalcsv = pd.concat([csv1, f1], axis=1) # 두 csv를 병합
        finalcsv = finalcsv.drop(finalcsv.columns[0:1], axis='columns')  # 첫번째 열 제거
        finalcsv.to_csv("C:\\Users\\br179\\PycharmProjects\\capstone\\APItest3.csv") # 최종적으로 저장
    break

print("end")
