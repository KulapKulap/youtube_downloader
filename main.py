import yt_dlp

def download_video(video_url, output_path="./"):
    try:
        # Set options for yt-dlp
        ydl_opts = {
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',  # Save video with title as filename
            'format': 'best',  # Download the best quality video
        }

        # Use yt-dlp to download the video
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("Downloading...")
            ydl.download([video_url])
            print(f"Download complete! Saved to: {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main execution
if __name__ == "__main__":
    # Prompt the user for the video URL
    url = input("enter video url: ")
    path = input("where to save? ") or "./"

    # Call the download function
    download_video(url, path)
