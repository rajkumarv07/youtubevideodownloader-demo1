from pytube import YouTube

video_url = input("Enter YouTube video URL: ")
try:
    yt = YouTube(video_url)
    yt.check_availability()
    stream = yt.streams.get_highest_resolution()
    stream.download()
    print(f"Downloaded: {yt.title}")
except Exception as e:
    print(f"Error: {str(e)}")
