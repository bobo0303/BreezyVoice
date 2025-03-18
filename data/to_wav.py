import os  
import subprocess  
  
def convert_mkv_to_wav(input_folder, output_folder):  
    # 確保輸出資料夾存在  
    if not os.path.exists(output_folder):  
        os.makedirs(output_folder)  
  
    # 遍歷資料夾中的所有檔案  
    for filename in os.listdir(input_folder):  
        if filename.endswith('.mp3'):  
            input_filepath = os.path.join(input_folder, filename)  
            output_filename = os.path.splitext(filename)[0] + '.wav'  
            output_filepath = os.path.join(output_folder, output_filename)  
  
            # 使用 ffmpeg 進行轉換  
            command = ['ffmpeg', '-i', input_filepath, '-vn', '-acodec', 'pcm_s16le', output_filepath]  
            subprocess.run(command)  
  
            print(f'Converted {input_filepath} to {output_filepath}')  
  
# 使用範例  
input_folder = 'data/'  
output_folder = 'data/'  
convert_mkv_to_wav(input_folder, output_folder)  