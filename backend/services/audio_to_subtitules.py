import whisper
import ffmpeg

def audio_to_subtitles(input_path, output_path):
    # Extraer audio del video
    output_audio = input_path+"_audio.wav"

    ffmpeg.input(input_path).output(output_audio, acodec="pcm_s16le", ar="16000").run()

    # Load the Whisper model
    model = whisper.load_model("base")

    # Transcribe the audio file
    result = model.transcribe(output_audio, fp16=False)

    # Write the subtitles to a file
    with open(output_path, 'w') as f:
        for segment in result['segments']:
            start = segment['start']
            end = segment['end']
            text = segment['text']
            f.write(f"{start:.2f} --> {end:.2f}\n{text}\n\n")
