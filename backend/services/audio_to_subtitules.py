import whisper
import os

def audio_to_subtitles(input_path, output_path):
    print(input_path)

    # Load the Whisper model
    model = whisper.load_model("base")

    print('model loaded')
    # Delete the existing .srt file if it exists
    if os.path.exists(output_path):
        os.remove(output_path)
        print(f"Deleted existing file: {output_path}")

    # Transcribe the audio file
    result = model.transcribe(input_path, fp16=False)
    print('result transcribed')

    # Check if transcription worked
    if 'segments' not in result:
        print("No subtitles generated!")
        return

    print('saving results')

    # Write the subtitles to a file
    with open(output_path, 'w', encoding="utf-8") as f:
        for segment in result['segments']:
            start = segment['start']
            end = segment['end']
            text = segment['text']
            f.write(f"{start:.2f} --> {end:.2f}\n{text}\n\n")

    #TODO, afegir qui es que parla
