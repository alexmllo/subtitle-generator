import whisper
import os
from simple_diarizer.diarizer import Diarizer

# Load Whisper Model
model = whisper.load_model("base")
print('Model loaded')

diarization = Diarizer(embed_model='xvec', cluster_method='sc')

def audio_to_subtitles(input_path, output_path):
    print(f"Processing: {input_path}")

    # Delete the existing .srt file if it exists
    if os.path.exists(output_path):
        os.remove(output_path)
        print(f"Deleted existing file: {output_path}")

    # Perform transcription with Whisper
    result = model.transcribe(input_path, fp16=False)
    print('Result transcribed')

    # Perform diarization
    diarization_segments = diarization.diarize(input_path, threshold=140)

    print('Diarization completed')

    # Write the subtitles in proper SRT format
    with open(output_path, 'w', encoding="utf-8") as f:
        for i, segment in enumerate(result['segments']):
            start = format_srt_time(segment['start'])
            end = format_srt_time(segment['end'])
            text = segment['text']

            # Identify speaker based on diarization results
            speaker = "Unknown"
            for seg in diarization_segments:
                seg_start = float(seg['start'])  # Convert numpy float64 to regular float
                seg_end = float(seg['end'])
                speaker_id = int(seg['label'])  # Convert numpy int32 to regular int

                if seg_start <= segment['start'] <= seg_end:
                    speaker = f"Speaker {speaker_id}"
                    break

            f.write(f"{i + 1}\n{start} --> {end}\n{speaker}: {text}\n\n")

    print(f"Subtitles saved to: {output_path}")

# Helper function to format timestamps in SRT format (hh:mm:ss,ms)
def format_srt_time(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    sec = int(seconds % 60)
    milliseconds = int((seconds % 1) * 1000)
    return f"{hours:02}:{minutes:02}:{sec:02},{milliseconds:03}"
