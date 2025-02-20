from moviepy.editor import VideoFileClip
import speech_recognition as sr
import os

def generate_subtitles(video_path):
    # Load the video file
    video = VideoFileClip(video_path)
    
    # Extract audio from the video
    audio_path = "temp_audio.wav"
    video.audio.write_audiofile(audio_path)

    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Load the audio file
    with sr.AudioFile(audio_path) as source:
        audio_data = recognizer.record(source)

    # Generate subtitles using Google Web Speech API
    try:
        text = recognizer.recognize_google(audio_data)
    except sr.UnknownValueError:
        text = "Could not understand audio"
    except sr.RequestError as e:
        text = f"Could not request results from Google Speech Recognition service; {e}"

    # Create .srt file
    srt_path = video_path.rsplit('.', 1)[0] + '.srt'
    with open(srt_path, 'w') as srt_file:
        srt_file.write("1\n")
        srt_file.write("00:00:00,000 --> 00:00:10,000\n")  # Placeholder timestamps
        srt_file.write(text + "\n\n")

    # Clean up temporary audio file
    os.remove(audio_path)

    return srt_path