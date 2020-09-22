import urllib.request
import json 
from apikey import apikey 
def getViews(VID_ID, apikey):
        url = 'https://www.googleapis.com/youtube/v3/videos?part=statistics&id='  + VID_ID + '&key=' + apikey
        req = urllib.request.Request(url)
        resp = urllib.request.urlopen(req)
        respData = resp.read()
        res = json.loads(respData.decode('utf-8'))
        statistics = res["items"][0]["statistics"]
        viewCount = statistics["viewCount"]
        return viewCount
#Example  https://www.youtube.com/watch?v=lfdw-RMF7yk&t=18s
#lfdw-RMF7yk&t=18s is the id we need 
url = input("Paste your youtubevideo id :")
print(getViews(url,apikey))
