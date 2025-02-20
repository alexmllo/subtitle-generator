const uploadForm = document.getElementById('uploadForm');
const videoInput = document.getElementById('videoInput');
const inputButton = document.getElementById('inputButton');

uploadForm.addEventListener('submit', async (event) => {
    event.preventDefault();

    inputButton.classList.add("loading")
    inputButton.innerText="Loading..."

     try {
        const formData = new FormData();
        formData.append('video', videoInput.files[0]);

        const videoName = videoInput.files[0].name.split('.')[0]

        const response = await fetch('/upload', {
            method: 'POST',
            body: formData
        });

         if (!response.ok) {
            const errorData = await response.json();
            alert(errorData.error);
            return;
        }

        // Create a blob URL for the file
        const blob = await response.blob();
        const downloadUrl = window.URL.createObjectURL(blob);

        // Create a temporary download link
        const a = document.createElement('a');
        a.href = downloadUrl;
        a.download = videoName + '.srt';
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);

        // Cleanup
        window.URL.revokeObjectURL(downloadUrl);

    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred while uploading the video.');
    } finally {
        inputButton.innerText="Upload Video"
        inputButton.classList.remove("loading")
    }
});