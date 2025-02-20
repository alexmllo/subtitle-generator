import whisper
import sys

def audio_to_subtitles(audio_path, output_path):
    # Load the Whisper model
    model = whisper.load_model("base")

    # Transcribe the audio file
    result = model.transcribe(audio_path, fp16=False)

    # Write the subtitles to a file
    with open(output_path, 'w') as f:
        for segment in result['segments']:
            start = segment['start']
            end = segment['end']
            text = segment['text']
            f.write(f"{start:.2f} --> {end:.2f}\n{text}\n\n")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python audio_to_subtitles.py <audio_path> <output_path>")
        sys.exit(1)

    audio_path = sys.argv[1]
    output_path = sys.argv[2]
    audio_to_subtitles(audio_path, output_path)