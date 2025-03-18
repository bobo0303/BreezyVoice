import pandas as pd  
  
# 讀取 CSV 文件  
input_csv = 'common_voice_speakers_917_wav/TCM_data_random.csv'  
df = pd.read_csv(input_csv)  
  
# 計算三等份的切分點  
mid_index1 = len(df) // 3  
mid_index2 = 2 * mid_index1  
  
# 將 DataFrame 拆分成三個部分  
df1 = df.iloc[:mid_index1]  
df2 = df.iloc[mid_index1:mid_index2]  
df3 = df.iloc[mid_index2:]  
  
# 將三個 DataFrames 保存成三個新的 CSV 文件，並保留標頭  
df1.to_csv('common_voice_speakers_917_wav/TCM_data_random_1.csv', index=False)  
df2.to_csv('common_voice_speakers_917_wav/TCM_data_random_2.csv', index=False)  
df3.to_csv('common_voice_speakers_917_wav/TCM_data_random_3.csv', index=False)  