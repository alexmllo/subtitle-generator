from flask import Flask, request, jsonify
import os
from services.subtitle_generator import generate_subtitles

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(message="Welcome to the Subtitle Generator web application!")

@app.route('/upload', methods=['POST'])
def upload_video():
    if 'video' not in request.files:
        return jsonify(error="No video file provided"), 400

    video_file = request.files['video']
    
    if video_file.filename == '':
        return jsonify(error="No selected file"), 400

    if video_file:
        video_path = os.path.join('uploads', video_file.filename)
        video_file.save(video_path)
        
        subtitles = generate_subtitles(video_path)
        
        srt_file_path = video_path.rsplit('.', 1)[0] + '.srt'
        with open(srt_file_path, 'w') as srt_file:
            srt_file.write(subtitles)

        return jsonify(message="Subtitles generated successfully!", srt_file=srt_file_path), 200

if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    app.run(debug=True)