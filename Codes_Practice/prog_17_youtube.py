
# import youtube_dl
import sys, string, os

lst = []

lst.append('https://www.youtube.com/watch?v=x4AaYr1t3TA')

for i in lst:
    path = i
    print path
    os.system('youtube-dl.exe %s' %path)

exit ()
ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s'})

with ydl:
    result = ydl.extract_info(
        'https://www.youtube.com/watch?v=HlHkLGTxCQs',
        download=False # We just want to extract the info
    )

if 'entries' in result:
    # Can be a playlist or a list of videos
    video = result[entries][0]
else:
    # Just a video
    video = result

print(video)
video_url = video[url]
print(video_url)