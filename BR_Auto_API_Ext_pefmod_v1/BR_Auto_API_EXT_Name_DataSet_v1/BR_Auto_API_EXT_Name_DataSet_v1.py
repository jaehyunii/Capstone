import pefile
import pandas as pd
import os
import sys
import numpy as np

## file_list
path1 = r'C:\Users\br179\exe' # 실제 exe 파일 저장장소
path_name = r'C:\Users\br179\exe_name' # exe파일 이름을 대조시키기위한 폴더
file_list2 = os.listdir(path_name)  # 파일경로에대한 모든파일을 도출
file_list3 = os.listdir(path1)
file_list4 = [file for file in file_list2 if file.endswith(".exe")] # exe파일 이름만 도출하기위한 코드
#' ' 뺀 file_list
file_list=[]
for i in file_list4:
    file_list.append(i[:-4])
file_list


# 프로그램별 api_list (API_List.csv)
api_list = pd.read_csv("C:\\Users\\br179\\api\\API_List.csv")
api_list = api_list.drop(api_list.columns[0:1], axis='columns')

# 중복제거된 모든 api_name (API_Name.csv)
api_name = pd.read_csv("C:\\Users\\br179\\api\\API_Name.csv")
api_name = api_name.drop(api_name.columns[0:1], axis='columns')

# api_list to type of list , 전체 api (column),
# ex)GetProcAddress', 'GetModuleHandleA', 'LoadLibraryA',...
# api name -> list
api_name_column = api_name.values.tolist()
api_name_column = np.ravel(api_name_column, order='C')

# api_name_dataset
data_set = pd.DataFrame(index=file_list2, columns=api_name_column)
# dataset에 값 채워 넣기
for i in file_list:
    f1 = api_list.loc[:,[i]].dropna()
    arr = f1.values.tolist()
    arr = np.ravel(arr,order='C')
    for j in api_name_column:
        if(j in arr):
            data_set.loc[i,j] = 1
        else:
            data_set.loc[i,j] = 0

# api별 각 api를 사용한 프로그램수 추가
for i in api_name_column:
    data_set.loc['used_Program_count',i]= int(data_set.loc[:,[i]].sum())

data_set.to_csv("C:\\Users\\br179\\api\\API_Name_DataSet.csv")

# 여기까지 프로그램수 찾기 위한 코드
# 아래부터 임계치 이상의 api에 대한 dataset 생성

# 임계치 이상의 api를 list에 추가
new_api=[]
for i in api_name_column:
    if(data_set.loc['used_Program_count',i]>=5): # 임계치 = 5
        new_api.append(i)

# 임계치 이상의 api에 대한 dataset
real_data_set = pd.DataFrame(index=file_list, columns=new_api)

for i in file_list:
    f1 = api_list.loc[:,[i]].dropna()
    arr = f1.values.tolist()
    arr = np.ravel(arr,order='C')
    for j in new_api:
        if(j in arr):
            real_data_set.loc[i,j] = 1
        else:
            real_data_set.loc[i,j] = 0

real_data_set.to_csv("C:\\Users\\br179\\api\\API_Name_DataSet_v1.csv")

print("----------")
print(" complete ")
print("----------")



