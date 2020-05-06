# -*- coding: utf-8 -*-
import os, sys

# exe_real_path = input("실행파일 경로 입력 : ")
# exe_cpr_path = input("비교할 실행파일 이름 경로 입력 : ")

exe_real_path = "D:\\Capstone_exe\\Multimedia" # 실제 exe 파일 저장장소
exe_cpr_path = "D:\\CPR_exe_name" # exe파일 이름을 대조시키기위한 폴더

Cpr_file_list = os.listdir(exe_cpr_path) # 비교 대상 exe파일 이름 list 생성

# if(len(real_file_list) != len(Cpr_file_list)):  # 실제 exe파일 저장소 exe갯수와 파일이름 대조 디렉토리 exe갯수가 동일한지 확인
#     print("exe_dir과 cpr_exe_dir의 파일 갯수가 다릅니다.")
# else : print("-------pass---------")

#대조 파일 리스트 서칭 & (root)real file list에 실행파일 존재하는지 확인-> 하위 디렉토리 파일리스트에 실행파일 존재하는지 확인

path_res = [] # path 저장소
def Pathsearch(exe_real_path,Cpr_file_list):
    for root, dirs, files in os.walk(exe_real_path):
        rootpath = os.path.join(os.path.abspath(exe_real_path),root) # join : 병합 // abspath : 절대 경로
        for file in files:
            if(file.endswith(".exe")):
                for s1 in Cpr_file_list:
                    if s1 in file:
                        filepath = os.path.join(rootpath, file)
                        os.path.normpath(filepath)
                        path_res.append(filepath)
    return path_res

Pathsearch(exe_real_path,Cpr_file_list)
print(path_res)





