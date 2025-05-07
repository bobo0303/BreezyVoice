# def remove_duplicates(input_file, output_file):  
#     try:  
#         with open(input_file, 'r', encoding='utf-8') as f:  
#             lines = f.readlines()  
  
#         # 去除每行的前後空格，並使用集合來過濾重複項  
#         unique_lines = set(line.strip() for line in lines)  
  
#         # 將無重複的內容寫回新的檔案  
#         with open(output_file, 'w', encoding='utf-8') as f:  
#             for line in sorted(unique_lines):  
#                 f.write(line + '\n')  
  
#         print(f"去除重複項後的結果已保存到 {output_file}")  
  
#     except Exception as e:  
#         print(f"處理檔案時發生錯誤: {e}")  
  
# # 使用範例如下  
# input_file = 'common_voice_speakers_917_wav/keep_audio_files.txt'  # 替換成你的輸入檔案名稱  
# output_file = 'output_without_duplicates.txt'  # 替換成你希望的輸出檔案名稱  
  
# remove_duplicates(input_file, output_file)  



# import csv  
# import os  
  
# # 文件路径  
# csv_file_path = 'common_voice_speakers_917_wav/TCM_data_random.csv'  
# keep_audio_files_path = 'output_without_duplicates.txt'  
  
# # 读取已存在的音频文件记录  
# with open(keep_audio_files_path, 'r') as file:  
#     existing_files = set(line.strip().split('/')[-1].replace('.wav', '') for line in file if line.strip())  
  
# # 读取 CSV 文件  
# rows_to_keep = []  
# header = []  
  
# with open(csv_file_path, 'r', encoding='utf-8') as csvfile:  
#     reader = csv.reader(csvfile)  
#     header = next(reader)  # 读取头行  
#     for row in reader:  
#         output_filename = row[-1]  
#         if output_filename not in existing_files:  
#             rows_to_keep.append(row)  
  
# # 检查已过滤的数据  
# print(f"总条目数: {len(rows_to_keep)} (剔除已存在的音频文件后)")  
  
# # 每份文件包含多少行数据  
# split_size = len(rows_to_keep) // 3
# remainder = len(rows_to_keep) % 3
  
# # 拆分并写入新的 CSV 文件  
# start_idx = 0  
# for i in range(3):  
#     end_idx = start_idx + split_size + (1 if i < remainder else 0)  
#     split_rows = rows_to_keep[start_idx:end_idx]  
  
#     split_file_path = f'TCM_data_random_{i+1}.csv'  
#     with open(split_file_path, 'w', encoding='utf-8') as split_file:  
#         writer = csv.writer(split_file)  
#         writer.writerow(header)  # 写入头行  
#         writer.writerows(split_rows)  
      
#     start_idx = end_idx  
  
#     print(f"{split_file_path} 已创建，包含 {len(split_rows)} 条数据")  