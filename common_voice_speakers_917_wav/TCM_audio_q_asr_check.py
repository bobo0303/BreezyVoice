import os  
import requests  
import jiwer  
import json  
import re  
import string
from opencc import OpenCC  
  
cc = OpenCC('s2t')  
  
file_path = '/mnt/common_voice_speakers_917_wav/colloquial_stt_training_data.json'  
with open(file_path, 'r', encoding='utf-8') as file:  
    data = json.load(file)  
  
audio_directory = '/mnt/TCM_results/'  
keep_file = '/mnt/common_voice_speakers_917_wav/keep_audio_files.txt'  
delete_file = '/mnt/common_voice_speakers_917_wav/delete_audio_files.txt'  
  
api_url = 'http://localhost:80/vst_translate'  
  
def remove_punctuation(text):  
    return text.translate(str.maketrans('', '', string.punctuation))  
  
def remove_pattern(text):  
    pattern = r'\[:ㄨㄛ4\]'  
    clean_text = re.sub(pattern, '', text)  
    return clean_text  
  
def transcribe_audio(file_path):  
    with open(file_path, 'rb') as f:  
        files = {'file': f}  
        payload = {  
            'audio_uid': '0',  
            'sample_rate': 16000,  
            'o_lang': 'zh',  
            't_lang': 'zh',  
            'timeout': 30  
        }  
        response = requests.post(api_url, files=files, params=payload)  
        if response.status_code == 200:  
            if response.json().get('status') == "FAILED":
                return None  
            else:
                return response.json().get('data')["ori_text"]  
        else:  
            print("Error:", response.text)  
            return None  
  
def calculate_cer(reference, hypothesis):  
    return jiwer.cer(reference, hypothesis)  
  
if __name__ == '__main__':  
    while True:  
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
  
        for root, dirs, files in os.walk(audio_directory):  
            for file in files:  
                if file.endswith('.wav'):  
                    file_path = os.path.join(root, file)  
  
                    if file_path in keep_files:  
                        continue  
 
                    if os.path.exists(file_path):  
                        transcription = transcribe_audio(file_path)                    
                    else:
                        transcription = None
                        
                    if transcription is None or "":  
                        continue  
                
                    if file_path in delete_files:  
                        delete_files.remove(file_path) 
                        with open(delete_file, 'w', encoding='utf-8') as df:  
                            for path in delete_files:  
                                df.write(f"{path}\n")  
  
                    transcription_traditional = cc.convert(transcription).rstrip('。')  
                    index = file[:-4].split('_')[-1]  
                    text = data[int(index)]['colloquial'].rstrip('。')  

                    text = remove_punctuation(text)
                    transcription_traditional = remove_punctuation(transcription_traditional)
                    # text = remove_pattern(text)  
                    print("GT: ", text)  
                    print("ASR: ", transcription_traditional)  
  
                    if text:  
                        cer = calculate_cer(text, transcription_traditional)  
                        print(f"File: {file_path}, CER: {cer}")  
  
                        if cer < 0.4:
                            with open(keep_file, 'a', encoding='utf-8') as kf:  
                                kf.write(f"{file_path}\n")  
                            keep_files.add(file_path)  
                        else:  
                            with open(delete_file, 'a', encoding='utf-8') as df:  
                                df.write(f"{file_path}\n")  
                            delete_files.add(file_path)  
                            if os.path.exists(file_path):  
                                os.remove(file_path)  
