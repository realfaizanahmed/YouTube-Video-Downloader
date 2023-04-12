# A PYTHON PROJECT TO DOWNLOAD YOUTUBE VIDEOS FORM THIS PYTHON CODE

from pytube import YouTube

link = "https://youtu.be/FOGRHBp6lvM"

yt1 = YouTube(link)

#Yoitube video title fetcher
print(yt1.title)

#YouTube Video Tumbnail fether
print(yt1.thumbnail_url)

#video downloader

videos = yt1.streams.all()

vid = list(enumerate(videos))
for i in vid:
    print(i)
print()

strm = int(input("enter video resolution index: "))
videos[strm].download()
print("Video Downloaded successfully")


