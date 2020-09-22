import urllib.request
import json 
import time
from PIL import Image
from PIL import ImageFont 
from PIL import ImageDraw

def get_views():
    views = 1000000
    return views 

def views_to_string(views): 
    ret = []

    curr = 0 
    v = str(views)[::-1]
    for idx, i in enumerate(v):
        if idx % 3 == 0 and idx > 0: 
            ret.append(",") 
        ret.append(i)
    
    return "".join(ret[::-1])

def create_thumbnail(views,likes,dislikes,comments):
    view_string = views_to_string(views)
    likes_string = views_to_string(likes)
    dislikes_string = views_to_string(dislikes)
    comments_string = views_to_string(comments)
    
    img = Image.open("sample-in.JPG")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("Corp-Bold.otf", 90)
    draw.text((620,100), view_string + " VIEWS", (50, 205, 50), font=font)
    draw.text((620,200), likes_string +" Likes", (50, 205, 50), font=font)
    draw.text((620,300), dislikes_string + " Dislikes", (50, 205, 50), font=font)
    draw.text((620,400), comments_string + " Comments", (50, 205, 50), font=font)
    img.save("thumbnail.jpg")
create_thumbnail(10,10,10,10)