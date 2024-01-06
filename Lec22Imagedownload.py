import random
import urllib.request


def download_web_images(url):
    name = random.randrange(1, 1000)
    full_filename = str(name) + ".jpg"
    urllib.request.urlretrieve(url, full_filename)


download_web_images("https://wallpapers.com/images/featured/john-wick-jeaidqurrfx52d3u.jpg")
