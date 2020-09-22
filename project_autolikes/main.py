from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from apikey import apikey
import time
class YoutubeBot:

    flow = InstalledAppFlow.from_client_secrets_file('client_secret.json', 'https://www.googleapis.com/auth/youtube.force-ssl')
    credentials = flow.run_console()
    youtube = build('youtube', 'v3', credentials=credentials)

    def getVids(self):
        ids = [] #stores the video ids
        channelId = "UCiBfuUreTbKvBKtQbb6SIWQ"
        maxResults = 2
        youtube = build('youtube', 'v3', developerKey=apikey)
        request = youtube.search().list(
            part="snippet",
            channelId=channelId,
            maxResults=maxResults,
            order="date",
            type="video")
        response = request.execute()
        for item in response['items']:
            print(item['snippet']['title'])
            ids.append((item['id']['videoId'], item['snippet']['channelId']))
        return ids

    def likeVids(self):
        ids = self.getVids()
        for videoId in ids:
            self.youtube.videos().rate(rating='like', id=videoId[0]).execute()
	
	
        
bot = YoutubeBot()
def main():
    while True:
        timeout = 86400
        bot.likeVids()
        time.sleep(timeout)
if __name__ == "__main__":
    main()
