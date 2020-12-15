import pytube

url = "https://www.youtube.com/watch?v=HBxCHonP6Ro&list=PL6gx4Cwl9DGAcbMi1sH6oAMk4JHw91mC_"

playList = pytube.playList(url)
for url in playList:
    video = pytube.YouTube(url)
    stream = video.streams.get_by_itag(22)
    stream.download()

