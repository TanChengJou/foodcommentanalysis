import pandas as pd
import time
from snownlp import sentiment



start = time.time()


sentiment.train('neg.txt', 'pos.txt')
sentiment.save("C:/Users/cna/AppData/Local/Programs/Python/Python36/Lib/site-packages/snownlp/sentiment/sentiment.marshal")

# 結束測量
end = time.time()

# 輸出結果
print("執行時間：%f 秒" % (end - start))
