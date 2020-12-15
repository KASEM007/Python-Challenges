import pytube

url = "https://www.youtube.com/watch?v=ztl8PLyqpYE"

video = pytube.YouTube(url)

stream = video.streams.get_by_itag(22)
print("Downloading...")
stream.download(filename="UFC 257")
print("Done")


# for stream in video.streams:
#     if "video" in str(stream) and "mp4" in str(stream):
#         print(stream)
