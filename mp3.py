from pytube import YouTube
import os 
from colorama import Fore

print()
link = input("Video linki: ") 
filepath = os.path.exists("mp3")

if not filepath:
    os.mkdir("mp3")

yt = YouTube(link)
# print(yt.streams.filter(only_audio=True))
stream = yt.streams.get_by_itag(140)
stream.download(output_path='./mp3',filename=yt.title+'.mp3')

print(Fore.CYAN + f"\n{yt.title}.mp3 indirildi!")
print(Fore.BLUE + "*"*39)
print("mp3 klasorunu kontrol edin :]")
print("*"*39)



