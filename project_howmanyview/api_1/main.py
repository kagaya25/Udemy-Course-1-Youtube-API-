import urllib.request
import json 
from api_1.apikey import apikey

def getViews(VID_ID):
        API_KEY = apikey
        url = 'https://www.googleapis.com/youtube/v3/videos?part=statistics&id='  + VID_ID + '&key=' + API_KEY
        req = urllib.request.Request(url)
        resp = urllib.request.urlopen(req)
        respData = resp.read()
        res = json.loads(respData.decode('utf-8'))
        print(url)
        print(res)
        statistics = res["items"][0]["statistics"]
        viewCount = statistics["viewCount"]
        likeCount = statistics["likeCount"]
        dislikeCount = statistics["dislikeCount"]
        commentCount = statistics["commentCount"]
        return viewCount , likeCount , dislikeCount , commentCount
#Example  https://www.youtube.com/watch?v=YwNlVeReXXc
#YwNlVeReXXc is the id we need 


