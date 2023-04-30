function showFileInfo() {
  var fileInput = document.getElementById('file-upload');
  var fileName = document.getElementById('file-name');
  var fileDuration = document.getElementById('file-duration');
  var fileSize = document.getElementById('file-size');
  var fileFormatWarning = document.getElementById('file-format-warning');
  var submitButton = document.querySelector('.submit-button');
  var audioPlayer = document.getElementById('audio-player');

  var file = fileInput.files[0];
  var fileType = file.type;
  var fileSizeMB = file.size / (1024 * 1024);

  // Clear the contents of the file name, duration, and size elements
  fileName.innerHTML = "";
  fileDuration.innerHTML = "";
  fileSize.innerHTML = "";

  fileName.innerHTML = "File name: " + file.name;

  var audio = new Audio();
  audio.src = URL.createObjectURL(file);
  audio.addEventListener('loadedmetadata', function() {
    setTimeout(function() {
      var duration = audio.duration;
      var minutes = Math.floor(duration / 60);
      var seconds = Math.round(duration % 60);
      fileDuration.innerHTML = "Duration: " + minutes + " minutes " + seconds + " seconds";
    }, 100); // Delay retrieval of duration by 100ms
  });

  fileSize.innerHTML = "File size: " + fileSizeMB.toFixed(2) + " MB";

  if (fileType != 'audio/wav') {
    fileFormatWarning.innerHTML = "Warning: Only .wav files are allowed, please choose file with correct format";
    fileFormatWarning.style.color = '#ff0000';
    fileFormatWarning.style.fontWeight = 700;
    submitButton.style.display = 'none';
    audioPlayer.innerHTML = "";
  } else {
    fileFormatWarning.innerHTML = "Correct file format, you can submit the file";
    fileFormatWarning.style.color = '#00b200';
    fileFormatWarning.style.fontWeight = 700;
    submitButton.style.display = 'block';

    // Create an audio player element and set its source to the uploaded file
    var audio = document.createElement('audio');
    audio.controls = true;
    audio.controlsList = 'nodownload';
    audio.src = URL.createObjectURL(file);
    audioPlayer.innerHTML = "";
    audioPlayer.appendChild(audio);
  }
}
