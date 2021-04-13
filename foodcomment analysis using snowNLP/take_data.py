import pandas as pd
import openpyxl
import os
import time

start = time.time()

#建立空字串
comment_data = []
#開啟檔案放置的資料夾
url = "./traindata/"
train_file = os.listdir(f'{url}')

#開啟檔案
for train_file_list in train_file:
    print(f'{train_file_list}資料處理')

    # 讀取資料，並將分數當作index
    data =pd.read_excel(
        f"{url}{train_file_list}",
        index_col=0
    ) 
    #取負向評論neg
    data = data.loc[[1,2,3],:]
    #取正向評論pos
    #data = data.loc[[4,5],:]

    #再把index回歸到從0開始的序列
    data = data.reset_index()
    for data_comment_index in range(data.shape[0]):
        comment = data.iloc[data_comment_index,1]
        comment_data.append(comment)

        

#存取成TXT檔案
with open ("neg.txt", 'w',encoding="utf-8") as f:
    f.write(str(comment_data))
# with open ("pos.txt", 'w',encoding="utf-8") as f:
#     f.write(str(comment_data))

end = time.time()
print("執行時間：%f 秒" % (end - start))
print("執行結束")
