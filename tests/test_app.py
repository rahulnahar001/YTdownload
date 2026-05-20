import unittest
from src.app import download_video  # Assuming download_video is the function to test

class TestApp(unittest.TestCase):

    def test_download_video_mp4(self):
        url = "https://www.youtube.com/watch?v=example"
        file_type = "mp4"
        quality = "720p"
        result = download_video(url, file_type, quality)
        self.assertTrue(result)  # Assuming the function returns True on success

    def test_download_video_mp3(self):
        url = "https://www.youtube.com/watch?v=example"
        file_type = "mp3"
        quality = "high"
        result = download_video(url, file_type, quality)
        self.assertTrue(result)  # Assuming the function returns True on success

    def test_invalid_url(self):
        url = "invalid_url"
        file_type = "mp4"
        quality = "720p"
        with self.assertRaises(ValueError):  # Assuming ValueError is raised for invalid URLs
            download_video(url, file_type, quality)

    def test_invalid_file_type(self):
        url = "https://www.youtube.com/watch?v=example"
        file_type = "invalid_type"
        quality = "720p"
        with self.assertRaises(ValueError):  # Assuming ValueError is raised for invalid file types
            download_video(url, file_type, quality)

    def test_invalid_quality(self):
        url = "https://www.youtube.com/watch?v=example"
        file_type = "mp4"
        quality = "invalid_quality"
        with self.assertRaises(ValueError):  # Assuming ValueError is raised for invalid quality options
            download_video(url, file_type, quality)

if __name__ == '__main__':
    unittest.main()