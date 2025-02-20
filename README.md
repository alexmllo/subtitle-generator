# Subtitle Generator Project

This project is a web application that allows users to upload videos and generate subtitles in .srt format using AI. It consists of a backend service built with Flask and a frontend application built with React.

## Project Structure

```
subtitle-generator
├── backend
│   ├── app.py                  # Entry point for the backend application
│   ├── requirements.txt         # Python dependencies for the backend
│   └── services
│       └── subtitle_generator.py # Logic for generating subtitles from videos
├── frontend
│   ├── public
│   │   └── index.html           # Main HTML file for the frontend
│   ├── src
│   │   ├── App.js               # Main component of the frontend application
│   │   ├── components
│   │   │   └── UploadButton.js   # Component for uploading video files
│   │   └── styles
│   │       └── App.css          # Styles for the frontend application
│   ├── package.json             # Configuration file for npm
└── README.md                    # Overall documentation for the project
```

## Setup Instructions

### Backend

1. Navigate to the `backend` directory.
2. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```
3. Run the backend application:
   ```
   python app.py
   ```

### Frontend

1. Navigate to the `frontend` directory.
2. Install the required npm packages:
   ```
   npm install
   ```
3. Start the frontend application:
   ```
   npm start
   ```

## Usage

1. Open your web browser and go to `http://localhost:3000` to access the frontend application.
2. Use the upload button to select a video file.
3. The application will send the video to the backend for processing and generate subtitles.
4. Once the subtitles are generated, you will be able to download the .srt file.

## Contributing

Feel free to contribute to this project by submitting issues or pull requests.