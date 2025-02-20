from flask import Flask, request, jsonify, send_from_directory, Response
import os
import re
from services.audio_to_subtitules import audio_to_subtitles

app = Flask(__name__, static_folder="../frontend", static_url_path="")

tmpPath = './uploads'

@app.route('/')
def home():
    return send_from_directory(app.static_folder, "index.html")

@app.route('/upload', methods=['POST'])
def upload_video():
    if 'video' not in request.files:
        return jsonify(error="No video file provided"), 400

    video_file = request.files['video']
    
    if video_file.filename == '':
        return jsonify(error="No selected file"), 400

    if video_file:
        video_path = os.path.join(tmpPath, re.sub(r'[^a-zA-Z0-9_/\\]', '_', video_file.filename))

        # Delete the existing .srt file if it exists
        if os.path.exists(video_path):
            os.remove(video_path)
            print(f"Deleted existing file: {video_path}")

        video_file.save(video_path)

        srt_file_path = video_path.split('.')[0]+'.srt'

        audio_to_subtitles(video_path, srt_file_path)

        # Stream the file and delete after it's fully sent
        def generate():
            with open(srt_file_path, 'rb') as f:
                yield from f  # Stream the file content

            # Now delete the files AFTER sending is complete
            try:
                os.remove(video_path)
                print(f"Deleted video file: {video_path}")
                os.remove(srt_file_path)
                print(f"Deleted subtitle file: {srt_file_path}")
            except Exception as e:
                print(f"Error deleting files: {e}")

        # Return streamed response
        return Response(generate(), content_type="text/plain", headers={
            "Content-Disposition": f"attachment; filename={os.path.basename(srt_file_path)}"
        })


if __name__ == '__main__':
    if not os.path.exists(tmpPath):
        os.makedirs(tmpPath)
    app.run(debug=True)