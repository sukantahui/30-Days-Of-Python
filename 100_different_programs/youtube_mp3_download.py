from pytube import YouTube
import os
import easygui
yt = YouTube(str(input("Enter the URL of the video you want to download: \n")))
  
# extract only audio
video = yt.streams.filter(only_audio=True).first()
  
# check for destination to save file
print("Enter the Destination, a dialogue box will open: ")
destination = easygui.diropenbox()

  
# download the file
mp3_file = video.download(output_path=destination)
  
# save the file
base, ext = os.path.splitext(mp3_file)
new_file = base + '.mp3'
os.rename(mp3_file, new_file)
  
# result of success
print(yt.title + " has been successfully downloaded.")