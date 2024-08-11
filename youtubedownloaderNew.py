import yt_dlp
import os

def download_video(url, download_location):
    # Ensure the download location exists, if not, create it
    if not os.path.exists(download_location):
        os.makedirs(download_location)

    # Define options for the download, including the output template
    ydl_opts = {
        'outtmpl': os.path.join(download_location, '%(title)s.%(ext)s')  # Save to specified location with video title as the filename
    }

    # Initialize the YoutubeDL object with the options
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # Download the video
        ydl.download([url])


if __name__ == "__main__":
    # Prompt the user to enter a YouTube URL
    url = input("Enter the YouTube URL: ")

    # Prompt the user to enter the preferred download location
    download_location = "/Users/zafarkamal/Downloads/youtubevideos/"

    # Call the download function with the provided URL and download location
    download_video(url, download_location)

    print("Download complete.")
