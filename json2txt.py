import json  
  
# 讀取 JSON 文件  
with open('APCL_data/data.json', 'r', encoding='utf-8') as f:  
    data = json.load(f)  
  
# 提取所有 "text" 字段的內容  
texts = []  
for item in data:  
    texts.extend(item['text'])  
  
# 將提取的內容寫入 TXT 文件  
with open('APCL.txt', 'w', encoding='utf-8') as f:  
    for line in texts:  
        f.write(line + '\n') 