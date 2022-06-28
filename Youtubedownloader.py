from pytube import YouTube

link = input("Enter the link:")

you_tube = YouTube(link)

print(f"\nTitle:{you_tube.title}")

print(f"Rating:{you_tube.rating}")

print(f"\nViews:{you_tube.views}")

print(f"\nVideo Length:{you_tube.length} seconds")

print(f"\nDescription:{you_tube.description}")

video = you_tube.streams.get_highest_resolution()

print("Downloading....")
video.download("downloads")
print("Download complete!")