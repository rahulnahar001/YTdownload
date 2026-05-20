# YouTube Video Downloader

This project is a simple web and command-line application that allows users to download videos from YouTube. Users can input a video URL, select the desired file type (MP3 or MP4), and choose the video quality option.

## Features

- Download YouTube videos by providing a video URL.
- Choose between MP3 and MP4 file formats.
- Select video quality options for downloads.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/youtube-video-downloader.git
   ```
2. Navigate to the project directory:
   ```
   cd youtube-video-downloader
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

### Web App

Run the web application:

```
python src/web_app.py
```

Then open http://127.0.0.1:5000 in your browser.

### Command Line

To run the application, use the command line interface:

```
python src/cli.py
```

Follow the prompts to input the video URL and select your desired options.

## Testing

To run the tests for the application, navigate to the project directory and run:

```
pytest tests/test_app.py
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.