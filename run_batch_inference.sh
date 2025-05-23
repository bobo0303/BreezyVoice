#!/bin/bash

# Default parameters
# CSV_FILE="data/batch_files.csv"
# SPEAKER_PROMPT_AUDIO_FOLDER="data"
# OUTPUT_AUDIO_FOLDER="results"

# APCL parameters
# CSV_FILE="APCL_data/APCL_dataset_S16_C49_P25.csv"
# SPEAKER_PROMPT_AUDIO_FOLDER="data"
# OUTPUT_AUDIO_FOLDER="APCL_results"

# TCM (traditional chinese medicine) parameters
CSV_FILE="123.csv"
SPEAKER_PROMPT_AUDIO_FOLDER="APCL_data"
OUTPUT_AUDIO_FOLDER="./"

# Run the Python script with default parameters
python batch_inference.py \
    --csv_file "$CSV_FILE" \
    --speaker_prompt_audio_folder "$SPEAKER_PROMPT_AUDIO_FOLDER" \
    --output_audio_folder "$OUTPUT_AUDIO_FOLDER"