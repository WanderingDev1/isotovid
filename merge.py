import os
from moviepy import VideoFileClip, AudioFileClip

video_input = "isotovideo.mp4" #or change to whatever you named it
audio_input = "isotoaudio.mp3" #or change to whatever you named it
video_output = "Merged.mp4" #change to the title you want

if not os.path.exists(video_input) or not os.path.exists(audio_input):
    print("Error: Make sure 'isotovideo.mp4' and 'isotoaudio.mp3' are in this folder!")
else:
    print("Loading the video and MP3 audio tracks...")
    video_clip = VideoFileClip(video_input)
    audio_clip = AudioFileClip(audio_input)
    
    print("Syncing video and audio tracks...")
    final_clip = video_clip.with_audio(audio_clip)
    
    print("🎬 Rendering your normal-speed glitch video layout...")
    final_clip.write_videofile(
        video_output, 
        codec="libx264", 
        audio_codec="aac",
        audio_bitrate="320k" 
    )
    
    video_clip.close()
    audio_clip.close()
    final_clip.close()
    
    print(f"\n🎉 SUCCESS! the video is ready here: '{video_output}'")
