const uploadForm = document.getElementById('uploadForm');
const videoInput = document.getElementById('videoInput');
const downloadLink = document.getElementById('downloadLink');

uploadForm.addEventListener('submit', async (event) => {
    event.preventDefault();

    const formData = new FormData();
    formData.append('video', videoInput.files[0]);

    try {
        const response = await fetch('/upload', {
            method: 'POST',
            body: formData
        });

        const data = await response.json();

        if (response.ok) {
            downloadLink.href = data.srt_file;
            downloadLink.style.display = 'block';
            downloadLink.innerText = 'Download Subtitles';
        } else {
            alert(data.error);
        }
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred while uploading the video.');
    }
});