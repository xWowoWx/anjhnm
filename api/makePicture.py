# -*- coding: utf-8 -*-
import cv2
import textwrap
from PIL import ImageFont, Image, ImageDraw
from pilmoji.source import AppleEmojiSource
from pilmoji import Pilmoji

def text_wrap(text, width):
    wrapper = textwrap.TextWrapper(width=width)
    word_list = wrapper.wrap(text=text)
    caption_new = ''
    for ii in word_list[:-1]:
        caption_new = caption_new + ii + '\n'
    caption_new += word_list[-1] + '\n'
    return caption_new

def write_pic(content, path):
    height = 500
    width = 800

    with Image.new('RGB', (width, height), (255, 255, 255)) as img:
        font = ImageFont.truetype(r"C:\Users\Administrator\AppData\Local\Microsoft\Windows\Fonts\jf-openhuninn-2.0.ttf", 40)

        content = text_wrap(content, 17)
        left, top, right, bottom = font.getmask(content).getbbox()
        right = font.getmask(content[:20]).getbbox()[2]
        bottom = (font.getmask(content[:20]).getbbox()[3] + 12) * content.count('\n')
        text_coordinate = int((width - (right - left)) / 2), int((height - (bottom - top)) / 2)

        with Pilmoji(img, source = AppleEmojiSource) as pilmoji:
            pilmoji.text(text_coordinate, content, font=font, fill=(0, 0, 0))

        img.save(path)
