from flask import Flask, request, jsonify, send_from_directory
import os
from services.audio_to_subtitules import audio_to_subtitles

app = Flask(__name__, static_folder="../frontend", static_url_path="")

tmpPath = 'C:/uploads'

@app.route('/')
def home():
    print("hi")
    return send_from_directory(app.static_folder, "index.html")

@app.route('/upload', methods=['POST'])
def upload_video():
    if 'video' not in request.files:
        return jsonify(error="No video file provided"), 400

    video_file = request.files['video']
    
    if video_file.filename == '':
        return jsonify(error="No selected file"), 400

    if video_file:
        video_path = os.path.join(tmpPath, video_file.filename)
        video_file.save(video_path)

        srt_file_path = video_path.rsplit('.', 1)[0] + '.srt'

        audio_to_subtitles(srt_file_path, srt_file_path)

        return jsonify(message="Subtitles generated successfully!", srt_file=srt_file_path), 200

if __name__ == '__main__':
    if not os.path.exists(tmpPath):
        os.makedirs(tmpPath)
    app.run(debug=True)