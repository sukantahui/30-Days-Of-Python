import sys
from pytube import YouTube
import os
import easygui
n = len(sys.argv)


yt = YouTube(str(input("Enter the URL of the video you want to download: \n")),use_oauth=True, allow_oauth_cache=True)
# yt = YouTube(str(sys.argv[1]),use_oauth=True, allow_oauth_cache=True)
  
# extract only audio
video = yt.streams.filter(only_audio=True).first()
  
# check for destination to save file
print("Enter the Destination, a dialogue box will open: ")
destination = easygui.diropenbox()
print(destination)
# destination="L:\MP3"
  
# download the file
mp3_file = video.download(output_path=destination)
  
# save the file
base, ext = os.path.splitext(mp3_file)
new_file = base + '.mp3'
os.rename(mp3_file, new_file)
  
# result of success
print(yt.title + " has been successfully downloaded.")