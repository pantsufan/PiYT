# YouTube Video Downloader and HTTP File Server
This repository contains two Python scripts that allow you to download YouTube videos using `yt-dlp` and serve files over HTTP using `http.server`.

## YouTube Video Downloader
The `main.py` script is a Python script that automates the process of downloading YouTube videos using `yt-dlp` command-line tool. It fetches the URLs of channels from a NewPipe subscription export JSON file and downloads the videos uploaded today and yesterday. The downloaded videos are saved in the specified output directory, organized into separate subdirectories for each channel.

To use the script:

1. Install `yt-dlp` by following the instructions at https://github.com/yt-dlp/yt-dlp.
2. Add `newpipe-subscriptions.json` containing the exported NewPipe subscription JSON data.
3. Adjust the `output_directory` variable in the script to specify the desired output directory path.
4. Run the script using: `python main.py`


## HTTP File Server
The `server.py` script is a Python script that starts a simple HTTP server using the `http.server` module. It serves files from a specified directory and provides a directory listing that includes files and subdirectories.

To use the script:

1. Adjust the `directory` and `port` variables in the script to specify the directory path and desired port number.
2. Execute the script using Python: `python server.py`.
4. Access the server by navigating to http://localhost:8000 (replace 8000 with the specified port number) in your web browser.

___ 
Please note that the provided scripts serve as examples and may require adjustments to fit your specific use case. Ensure that you have the necessary dependencies installed and review the script code for any additional configuration or customization options.

If you encounter any issues or have further questions, please feel free to reach out for support.

Enjoy downloading YouTube videos and serving files over HTTP with ease!
