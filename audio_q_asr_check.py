import os  
import requests  
import jiwer  
import json  
  
file_path = '/mnt/data/data.json'  
with open(file_path, 'r', encoding='utf-8') as file:  
    data = json.load(file)  
  
audio_directory = '/mnt/APCL_results/'  
# 要保存結果的檔案名稱  
keep_file = 'keep_audio_files.txt'  
delete_file = 'delete_audio_files.txt'  
  
if os.path.exists(keep_file):  
    with open(keep_file, 'r', encoding='utf-8') as kf:  
        keep_files = set(kf.read().splitlines())  
else:  
    keep_files = set()  
  
if os.path.exists(delete_file):  
    with open(delete_file, 'r', encoding='utf-8') as df:  
        delete_files = set(df.read().splitlines())  
else:  
    delete_files = set()  
  
# API 的 URL  
api_url = 'http://52.163.254.238/vst_translate'  
  
# 固定的 API 參數  
api_params = {  
    'audio_uid': '0',  
    'sample_rate': 16000,  
    'o_lang': 'zh',  
    't_lang': 'zh',  
    'timeout': 10  
}  
  
def transcribe_audio(file_path):  
    with open(file_path, 'rb') as f:  
        files = {'file': f}  
        response = requests.post(api_url, params=api_params, files=files)  
        if response.status_code == 200:  
            return response.json().get('transcription', '')  
        else:  
            return None  
  
def calculate_wer(reference, hypothesis):  
    return jiwer.wer(reference, hypothesis)  
  
for root, dirs, files in os.walk(audio_directory):  
    for file in files:  
        if file.endswith('.wav'):  
            file_path = os.path.join(root, file)  
              
            # 檢查音檔是否已經處理過  
            if file_path in keep_files:  
                continue  
              
            # 如果音檔在 delete_file 中，且音檔依然存在，重新判斷  
            if file_path in delete_files:  
                if os.path.exists(file_path):  
                    delete_files.remove(file_path)  
                else:  
                    continue  
              
            transcription = transcribe_audio(file_path)  
              
            classes = file[:-4].split('_')[1]  
            index = file[:-4].split('_')[2]  
            text = data[int(classes[1:])-1]['text'][int(index)] + "。"  
  
            if text:  
                wer = calculate_wer(text, transcription)  
                print(f"File: {file_path}, WER: {wer}")  
  
                if wer < 0.5:  
                    with open(keep_file, 'a', encoding='utf-8') as kf:  
                        kf.write(f"{file_path}\n")  
                    keep_files.add(file_path)  
                else:  
                    with open(delete_file, 'a', encoding='utf-8') as df:  
                        df.write(f"{file_path}\n")  
                    delete_files.add(file_path)  