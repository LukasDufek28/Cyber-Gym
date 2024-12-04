document.addEventListener("DOMContentLoaded", () => {
    const videoElement = document.getElementById("background-video");

    // Videos
    const videoSources = [
        "static/videos/video1.mp4",
        "static/videos/video2.mp4",
        "static/videos/video3.mp4",
        "static/videos/video4.mp4"
    ];

    let currentVideoIndex = 0;

    // Function to change the video source
    const changeVideo = () => {
        currentVideoIndex = (currentVideoIndex + 1) % videoSources.length;
        videoElement.src = videoSources[currentVideoIndex];
        videoElement.play();
    };

    // Change video
    setInterval(changeVideo, 5000);
});
