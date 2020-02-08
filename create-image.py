# coding=utf-8

import sys
import urllib.request
from os import path
from PIL import Image, ImageFont, ImageDraw

FONT_PATH = path.dirname(path.abspath(__file__)) + '/mplus-2p-heavy.ttf'
FONT = ImageFont.truetype(FONT_PATH, 24, encoding='unic')
IMAGE_FILE = path.dirname(path.abspath(__file__)) + '/image.png'


def get_artwork(url):
    urllib.request.urlretrieve(url, 'artwork.jpg')


def get_text_length(text):
    return FONT.getsize(text)[0]


def create_image(text):
    image = Image.new(
        "RGB", (64 + 32 + get_text_length(text) + 64, 32), (0, 0, 0))
    draw = ImageDraw.Draw(image)
    draw.font = FONT
    draw.text((64 + 32, 0), text, (255, 255, 255))

    artwork = Image.open('artwork.jpg')
    artwork = artwork.resize((32, 32))
    image.paste(artwork, (64, 0))
    return image


URL = sys.argv[1]
ARTIST = sys.argv[2]
TITLE = sys.argv[3]

get_artwork(URL)
create_image(' ' + ARTIST + '「' + TITLE + '」').save('image.jpg', quality=100)
