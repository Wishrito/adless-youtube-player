const video = document.getElementById('video');
const playPauseBtn = document.getElementById('play-pause');
const playIcon = document.getElementById('play-icon');
const pauseIcon = document.getElementById('pause-icon');
const seekBar = document.getElementById('seek');
const timeDisplay = document.getElementById('time-display');
const muteBtn = document.getElementById('mute');
const volumeBar = document.getElementById('volume');
const fullscreenBtn = document.getElementById('fullscreen');

function formatTime(seconds) {
    const min = Math.floor(seconds / 60);
    const sec = Math.floor(seconds % 60);
    return `${min.toString().padStart(2, '0')}:${sec.toString().padStart(2, '0')}`;
}

// Lecture / Pause
playPauseBtn.addEventListener('click', () => {
    if (video.paused) {
        video.play();
    } else {
        video.pause();
    }
});

video.addEventListener('play', () => {
    playIcon.style.display = 'none';
    pauseIcon.style.display = 'inline';
});

video.addEventListener('pause', () => {
    playIcon.style.display = 'inline';
    pauseIcon.style.display = 'none';
});

// Mise à jour de la barre de progression et du temps
video.addEventListener('timeupdate', () => {
    const value = (100 / video.duration) * video.currentTime;
    seekBar.value = value;
    timeDisplay.textContent = `${formatTime(video.currentTime)} / ${formatTime(video.duration)}`;
});

// Seek
seekBar.addEventListener('input', () => {
    const time = video.duration * (seekBar.value / 100);
    video.currentTime = time;
});

// Mute
muteBtn.addEventListener('click', () => {
    video.muted = !video.muted;
    muteBtn.textContent = video.muted ? '🔇' : '🔈';
});

// Volume
volumeBar.addEventListener('input', () => {
    video.volume = volumeBar.value;
});

fullscreenBtn.addEventListener('click', () => {
    if (!document.fullscreenElement) {
        video.parentElement.requestFullscreen().catch(err => {
            alert(`Erreur de plein écran : ${err.message}`);
        });
    } else {
        document.exitFullscreen();
    }
});
