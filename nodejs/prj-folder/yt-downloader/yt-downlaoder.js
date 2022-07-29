LINKS = [

    "phjGQZh5oms"

]

var YoutubeMp3Downloader = require("youtube-mp3-downloader");

//Configure YoutubeMp3Downloader with your settings
var YD = new YoutubeMp3Downloader({
    "ffmpegPath": "C:/FFmpeg/bin/ffmpeg.exe",        // FFmpeg binary location
    "outputPath": "C:/Users/Gaming_Dator_VII/Desktop/Mitt-repo/nodejs/prj-folder/yt-downloader/mp3s",    // Output file location (default: the home directory)
    "youtubeVideoQuality": "highestaudio",  // Desired video quality (default: highestaudio)
    "queueParallelism": 2,                  // Download parallelism (default: 1)
    "progressTimeout": 2000,                // Interval in ms for the progress reports (default: 1000)
    "allowWebm": false                      // Enable download from WebM sources (default: false)
});


for(let i = 0; i < LINKS.length; i++){
    download(LINKS[i])
}

function download(link){
    //Download video and save as MP3 file
    YD.download(link);

    YD.on("finished", function(err, data) {
        console.log(`\nFinished!\n${data.videoTitle}`);
    });

    YD.on("error", function(error) {
        console.log(error);
    });

    YD.on("progress", function(progress) {
        console.log(`${Math.round(progress.progress.percentage)}% Done.`);
    });    
}
