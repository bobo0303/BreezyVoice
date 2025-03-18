import json  
import csv
  
file_path = '/mnt/data/colloquial_stt_training_data.json'  
with open(file_path, 'r', encoding='utf-8') as file:  
    data = json.load(file)  
  
file_path = '/mnt/data/speaker_text.json'  
with open(file_path, 'r', encoding='utf-8') as file:  
    speakers = json.load(file)  
  
output_csv_path = '/mnt/data/TCM_data.csv'  
with open(output_csv_path, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['speaker_prompt_audio_filename', 'speaker', 'speaker_prompt_text_transcription', 'content_to_synthesize', 'output_audio_filename']  
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)  
    writer.writeheader()  
    
    for speaker in speakers:  
        speaker_prompt_audio_filename = speaker  
        # if speaker_prompt_audio_filename not in ["speaker002"]:
        #     continue
        speaker_prompt_text_transcription = speakers[speaker]  
        for index, classes in enumerate(data):  
            text = classes['colloquial']
            if text[-1] != "。":
                content_to_synthesize = text+"。"  
            output_audio_filename = f"{speaker}_{index}"  
            writer.writerow({  
                'speaker_prompt_audio_filename': speaker_prompt_audio_filename,  
                'speaker': speaker,  
                'speaker_prompt_text_transcription': speaker_prompt_text_transcription,  
                'content_to_synthesize': content_to_synthesize,  
                'output_audio_filename': output_audio_filename  
            })  
            
            
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
            
