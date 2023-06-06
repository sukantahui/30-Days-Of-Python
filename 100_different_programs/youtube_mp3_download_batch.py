import sys
from pytube import YouTube
import os
import easygui
n = len(sys.argv)

file=open("mp3_list.txt","r")
data=file.readlines()

count = 0
downloaded = 0
for i in data:
    # if not i:
    #     continue
    yt = YouTube(str(i.strip()),use_oauth=True, allow_oauth_cache=True)
    # yt = YouTube(str(input("Enter the URL of the video you want to download: \n")),use_oauth=True, allow_oauth_cache=True)

    # yt = YouTube(str(sys.argv[1]),use_oauth=True, allow_oauth_cache=True)
    
    # extract only audio
    video = yt.streams.filter(only_audio=True).first()
    
    # check for destination to save file
    # print("Enter the Destination, a dialogue box will open: ")
    # destination = easygui.diropenbox()
    # print(destination)
    destination="L:\MP3"
    count=count+1
    try:
         # download the file
        mp3_file = video.download(output_path=destination)
    
        # save the file
        base, ext = os.path.splitext(mp3_file)
        new_file = base + '.mp3'
        os.rename(mp3_file, new_file)
        
        print(str(count) + ". " + yt.title + " has been successfully downloaded.")
        downloaded+=1
    except FileExistsError:
        print("File already exists ",count," " , i)
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)
        print(ex)
        
   
   

    
print("Total Downloaded: " + str(downloaded))    
