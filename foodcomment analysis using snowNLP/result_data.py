import pandas as pd
from snownlp import SnowNLP
import openpyxl
import os
import time

start = time.time()

#取第一層路徑
url="./cleardata/"

#開啟第一層資料夾
document = os.listdir(f"{url}")

#第二層
for document_file in document:
    print(f'開啟資料夾----{document_file}')
    #開啟各類別資料夾
    document_shop = os.listdir(f"{url}{document_file}")
    #創建相同名稱的資料夾
    os.mkdir(f"./resultdata/{document_file}_分數")
    #第三層 
    for document_name in document_shop:
        print(f'{document_name}-----處理中')
        #開啟資料
        data = pd.read_excel(f'{url}{document_file}/{document_name}') 

        #建立空字串     
        Total_score = []   
        service_score = []
        environment_score = []
        food_score = []
        
        try:
            #總分 
            #最長的欄位，當作列的索引值
            for document_index in range(data.shape[0]):
                #依照列的索引，取的每一個評論欄位的字串
                comment_Total = data.iloc[document_index,1]  
                #載入評論  
                comment_Total = SnowNLP(comment_Total)
                comment_Total = comment_Total.sentiments-0.5
                #進行評論情感分析，並取小數點後兩位
                comment_score_Total = round(comment_Total,2)  
                #將數據加入空字串
                Total_score.append(comment_score_Total)
            data.insert(2,"Total_score",Total_score)

            #環境
            for document_index in range(data.shape[0]):  
                comment_environment = data.iloc[document_index,3]
                if type(comment_environment).__name__=="float":
                    environment_score.append("")
                else:
                    comment_environment = SnowNLP(comment_environment)
                    comment_environment = comment_environment.sentiments-0.5     
                    comment_score_environment = round(comment_environment,2)  
                    environment_score.append(comment_score_environment)
            data.insert(4,"environment_score",environment_score)

            #服務
            for document_index in range(data.shape[0]):  
                comment_service = data.iloc[document_index,5]
                if type(comment_service).__name__=="float":
                    service_score.append("")
                else:   
                    comment_service = SnowNLP(comment_service)
                    comment_service = comment_service.sentiments-0.5     
                    comment_score_service = round(comment_service,2)  
                    service_score.append(comment_score_service)
            data.insert(6,"service_score",service_score)

            #食物
            for document_index in range(data.shape[0]):  
                comment_food = data.iloc[document_index,7]
                if type(comment_food).__name__=="float":
                    food_score.append("")
                else:  
                    comment_food = SnowNLP(comment_food) 
                    comment_food = comment_food.sentiments-0.5    
                    comment_score_food = round(comment_food,2)  
                    food_score.append(comment_score_food)   
            data.insert(8,"food_score",food_score)

            #將檢測結果之excel檔案存放進去
            data.to_excel(f"./resultdata/{document_file}_分數/{document_name}",index=False)    
        except Exception as e:
            print(f"{document_name}發生錯誤: {e}，請重新檢查。")       
        
    print(f'資料夾 {document_file}  -----處理結束')

end = time.time()
print("執行時間：%f 秒" % (end - start))
print("執行結束")