import pytube

video_list = []

print("Enter URLs (terminate by 'stop')")
while True:
    url = input("")
    if url == "stop":
        break
    video_list.append(url)

for x, video in enumerate(video_list):
    v = pytube.YouTube(video)
    stream = v.streams.get_by_itag(22)
    print(f"Downloading video {x}...")
    stream.download()
    print("Done")
