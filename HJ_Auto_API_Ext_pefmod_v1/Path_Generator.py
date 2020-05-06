# -*- coding: utf-8 -*-
import pandas as pd
import os
import pefile
import Path_Generator_Mult
import time
start = time.time()  # 시작 시간 저장
csv_total_num_path = "D:\\csv\\API_total.csv"
csv_all_api_path= "D:\\csv\\APItest3.csv"
text_path = "D:\\text\\"
a= [] #csv파일을 만들기위한 dataFrame형식을 만들기위해 빈 배열 생성
j=0
a1 = pd.DataFrame(a) #dataFrame 생성
a1.to_csv(csv_all_api_path)  # 저장할 csv파일 생성
a1.to_csv(csv_total_num_path)  # 저장할 csv파일 생성

# exe_real_path = input("실행파일 경로 입력 : ")
# exe_cpr_path = input("비교할 실행파일 이름 경로 입력 : ")

exe_real_path = "D:\\Capstone_exe\\Multimedia" # 실제 exe 파일 저장장소
exe_cpr_path = "D:\\CPR_exe_name" # exe파일 이름을 대조시키기위한 폴더

Cpr_file_list = os.listdir(exe_cpr_path) # 비교 대상 exe파일 이름 list 생성

#대조 파일 리스트 서칭 & (root)real file list에 실행파일 존재하는지 확인-> 하위 디렉토리 파일리스트에 실행파일 존재하는지 확인

Path_Generator_Mult.Pathsearch(exe_real_path, Cpr_file_list) #path generation

for path in Path_Generator_Mult.path_res : # 변수 i에 file_list에 있는 string을 불러온다 , 이때 폴더설정에서 파일에 대한 확장자가 표기되어야함 없을시에는 .exe를 붙여줘야함


        pe = pefile.PE(path)                    # pefile경로를 각파일에대한 경로로 설정

        file = open(text_path+Cpr_file_list[j][:-4]+".txt", 'w') # API_name.txt를 생성

        pe.parse_data_directories()

        file.write( Cpr_file_list[j][:-4] + "\n")  #각 열에대한 exe파일이름을 추가하여 열 구분, i[:-4]는 .exe를 빼고 이름을 넣기위함 ex) kakao.exe -> kakao
        for entry in pe.DIRECTORY_ENTRY_IMPORT:  # txt파일에 api목록들을 넣음 // dataframe을 쉽게 나누기위해 줄바꿈단위로 입력함
            # file.write("'" + str(entry.dll)[2:] + "\n")
            for imp in entry.imports:
                if str(imp.name) != 'None':
                    file.write(str(imp.name) + "\n")

        file.close()

        f1 = pd.read_csv(text_path+Cpr_file_list[j][:-4]+".txt", delimiter='\t')  # APIList3.txt를 줄바꿈단위로 pandas로 csv를 읽음

        f2 = f1[Cpr_file_list[j][:-4]].value_counts() # 중복된 api 횟수를 count하기 위한 함수 -> dataframe이 아닌 series형태
        df1 = pd.DataFrame(data=f2.index, columns=['api name'])
        df2 = pd.DataFrame(data=f2.values, columns=['counter'])
        df = pd.merge(df1, df2, left_index=True, right_index=True) # Series를 dataframe type으로 바꿔줌
        df.to_csv("D:\\counter\\"+Cpr_file_list[j][:-4]+"_count.csv")

        f1.duplicated()
        f1 = f1.drop_duplicates() # datatframe에서 중복된 값 처리
        f3 = pd.DataFrame({'program name': [Cpr_file_list[j][:-4]], "api amount" : [len(f1)]}) # 프로그램별 api 갯수
        csv1 = pd.read_csv(csv_all_api_path) #처음에 생성한 빈 파일을 csv로 불러옴, 저장되잇던 csv파일 불러옴
        csv1.drop(csv1.columns[0:1], axis='columns') # 첫번째 열 제거 (열번호가 적혀서 출력되어 병합할때 문제가 생김)
        csv2 = pd.read_csv(csv_total_num_path)
        csv2.drop(csv1.columns[0:1], axis='columns')

        finalcsv = pd.concat([csv1, f1], axis=1) # 두 csv를 병합
        finalcsv = finalcsv.drop(finalcsv.columns[0:1], axis='columns')  # 첫번째 열 제거
        finalcsv2 = pd.concat([csv2, f3])  # 두 csv를 병합
        finalcsv2 = finalcsv2.drop(finalcsv2.columns[0:1], axis='columns')  # 첫번째 열 제거
        finalcsv.to_csv(csv_all_api_path) # 최종적으로 저장
        finalcsv2.to_csv(csv_total_num_path)  # 최종적으로 저장
        j=j+1

print("----------")
print(" complete ")
print("----------")

print("time :", time.time() - start)