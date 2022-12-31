from pytube import YouTube
import re




def getVideo(link):  
  try:
    if not checkUrl(link[0]):
     return "После команды /video должна быть ссылка на видео"
    yt = YouTube(link[0])     
    return yt.streams.filter(progressive=True, file_extension='mp4').desc().first().download()
  except:
    return False

def getAudio(link): 
  try:
    if not checkUrl(link[0]):
     return "После команды /audio должна быть ссылка на видео" 
    yt = YouTube(link[0]) 
    return yt.streams.filter(only_audio=True).desc().first().download()
  except:
    return False

def checkUrl(link):
  if re.search("(?P<url>https?://[^\s]+)", link):
    return True
  return False  


  
   


