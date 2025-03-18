import json  
import csv  
  
# 載入兩個 JSON 檔案  
file_path = '/mnt/common_voice_speakers_917_wav/colloquial_stt_training_data.json'  
with open(file_path, 'r', encoding='utf-8') as file:  
    data = json.load(file)  
  
file_path = '/mnt/common_voice_speakers_917_wav/common_voice_speakers_917.json'  
with open(file_path, 'r', encoding='utf-8') as file:  
    speakers = json.load(file)  
  
# 建立 CSV 檔案  
output_csv_path = '/mnt/TCM_data.csv'  
with open(output_csv_path, 'w', newline='', encoding='utf-8') as csvfile:  
    fieldnames = ['speaker_prompt_audio_filename', 'speaker', 'speaker_prompt_text_transcription', 'content_to_synthesize', 'output_audio_filename']  
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)  
  
    writer.writeheader()  
  
    # 使用集合 (set) 來追蹤已經寫入的記錄，避免重複  
    seen_records = set()  
  
    for speaker in speakers:  
        sentence = speaker['sentence']  
        speaker_wav = speaker['audio'][:-4]  # 去掉音頻檔案的副檔名  
  
        for index, classes in enumerate(data):  
            text = classes['colloquial']  
            if "\n" in text:  
                text = text.replace("\n", "")  
  
            if text[-1] != "。":  
                content_to_synthesize = text + "。"  
            else:  
                content_to_synthesize = text  
  
            output_audio_filename = f"{speaker_wav}_{index}"  
  
            # 檢查此記錄是否已經出現過  
            record_tuple = (speaker_wav, speaker_wav, sentence, content_to_synthesize, output_audio_filename)  
            if record_tuple not in seen_records:  
                writer.writerow({  
                    'speaker_prompt_audio_filename': speaker_wav,  
                    'speaker': speaker_wav,  
                    'speaker_prompt_text_transcription': sentence,  
                    'content_to_synthesize': content_to_synthesize,  
                    'output_audio_filename': output_audio_filename  
                })  
                # 加入到已見記錄集合  
                seen_records.add(record_tuple)  
            
            
# import json  
# import csv
  
# file_path = '/mnt/data/data.json'  
# with open(file_path, 'r', encoding='utf-8') as file:  
#     data = json.load(file)  
  
# file_path = '/mnt/data/speaker_text.json'  
# with open(file_path, 'r', encoding='utf-8') as file:  
#     speakers = json.load(file)  
  
# output_csv_path = '/mnt/data/APCL_dataset_S16_C49_P25.csv'  
# with open(output_csv_path, 'w', newline='', encoding='utf-8') as csvfile:
#     fieldnames = ['speaker_prompt_audio_filename', 'speaker', 'speaker_prompt_text_transcription', 'content_to_synthesize', 'output_audio_filename']  
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)  
#     writer.writeheader()  
    
#     for speaker in speakers:  
#         speaker_prompt_audio_filename = speaker  
#         # if speaker_prompt_audio_filename not in ["speaker002"]:
#         #     continue
#         speaker_prompt_text_transcription = speakers[speaker]  
#         for classes in data:  
#             for index, text in enumerate(classes['text']):  
#                 content_to_synthesize = text+"。"  
#                 output_audio_filename = f"{speaker}_{classes['Class']}_{index}"  
#                 writer.writerow({  
#                     'speaker_prompt_audio_filename': speaker_prompt_audio_filename,  
#                     'speaker': speaker,  
#                     'speaker_prompt_text_transcription': speaker_prompt_text_transcription,  
#                     'content_to_synthesize': content_to_synthesize,  
#                     'output_audio_filename': output_audio_filename  
#                 })  
            
