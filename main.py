import subprocess
import datetime
import os
import json

# Define the output directory where the videos will be saved
output_directory = f"Output"

# Define the path to the NewPipe subscription export JSON file
newpipe_export_file = "newpipe-subscriptions.json"

# Get the current date and yesterday's date
today = datetime.date.today().strftime("%Y%m%d")
yesterday = (datetime.date.today() - datetime.timedelta(days=1)).strftime("%Y%m%d")

# Read the NewPipe subscription export JSON file
with open(newpipe_export_file, "r") as file:
    json_data = json.load(file)

# Function to download videos for a channel
def download_videos(channel_data):
    # Extract channel URL and name
    channel_url = channel_data["url"] + "/videos"
    channel_name = channel_data["name"]

    # Construct the output directory for the channel
    channel_output_directory = output_directory

    # Create the channel's output directory if it doesn't exist
    os.makedirs(channel_output_directory, exist_ok=True)

    # Construct the command to download videos using yt-dlp
    command = f"yt-dlp --download-archive archive.txt --playlist-end 3 --dateafter {yesterday} --datebefore {today} -f 248+251/303+251 --write-sub --write-auto-sub --sub-format srt/best --sub-lang en --embed-subs -o {channel_output_directory}/%(uploader)s/%(upload_date)s_%(title)s.%(ext)s' --sponsorblock-remove all --merge-output-format mkv {channel_url}"

    try:
        # Execute the command asynchronously
        process = subprocess.Popen(command, shell=True)
        print(f"Download started for channel: {channel_name}")
        return process
    except subprocess.SubprocessError as e:
        print(f"An error occurred while starting the download for channel: {channel_name}")
        print(f"Error message: {e}")
        return None

# List to keep track of ongoing download processes
download_processes = []

# Iterate through each channel in the JSON data and start the downloads
for channel_data in json_data["subscriptions"]:
    process = download_videos(channel_data)
    if process is not None:
        download_processes.append(process)

# Wait for all download processes to complete
for process in download_processes:
    process.wait()

# All downloads completed, exit the script
print("All video downloads completed.")
exit(0)
