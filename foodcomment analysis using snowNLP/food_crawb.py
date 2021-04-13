import requests 
import json
from pandas import DataFrame
import openpyxl
import random
import time

# 超連結  記得改網址
url_first="https://www.google.com.tw/maps/preview/review/listentitiesreviews?authuser=0&hl=zh-TW&gl=tw&pb=!1m2!1y3765761102422063449!2y16295602441366766356!2m2!1i10!2i10!3e2!4m5!3b1!4b1!5b1!6b1!7b1!5m2!1so8vlX-NNqZivvA-R6L9Q!7e81"

a=url_first.split("1i10")

#建立兩個空字串，之後添加資料進去
score=[]
comment=[]
try:
    for sec in range(1,51):
        url_sec=a[0]+"1i"+str(sec)+"0"+a[1]
        text_sec = requests.get(url_sec).text
        pretext = ')]}\''
        text_sec = text_sec.replace(pretext,'')
        soup_sec = json.loads(text_sec)
        sec_list = soup_sec[2]
        for sec_data in sec_list:
            score.append(sec_data[4])
            comment.append(sec_data[3])
    #每次取完，時間隨機停留
        sleep_time=random.uniform(5,10)
        print(f"先停留{sleep_time}秒...{(sec)*10}篇抓取結束")
        time.sleep(sleep_time)
except Exception as e:
    print(f"發生錯誤於{(sec+1)*10}篇抓取時,錯誤為")
    print(e)

#將字串輸出成檔案
data={
    "分數":score,
    "評論":comment,
}
df=DataFrame(data)
df.to_excel("記得改名字.xlsx")
print("結束")
#df.to_csv("new3.csv")