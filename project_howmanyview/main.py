from api_1.main import getViews
from make_thumbnail.main import create_thumbnail
from updateTitle.main import changeVideoTitle
from update_thumbnail.main import update_thumbnail
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import google_auth_oauthlib.flow
import time


ID = "lfdw-RMF7yk" # This is the youtube video ID 

flow = InstalledAppFlow.from_client_secrets_file('client_secret.json', 'https://www.googleapis.com/auth/youtube.force-ssl')
credentials = flow.run_console()
youtube = build('youtube', 'v3', credentials=credentials)

def main():
    viewcount = 0
    likes = 0
    dislikes = 0
    comments = 0
    while True: 
        timeout = 120 
        # STEP 1: Get Video Views
        statistics = getViews(ID)
        current_views = statistics[0]
        if int(current_views) > int(viewcount): 
            # STEP 2: Create New Thumbnail  
            create_thumbnail(current_views,statistics[1],statistics[2],statistics[3])
            # STEP 3: Update Video Thumbnail and Title # need the id here
            changeVideoTitle(ID,current_views,youtube)
            update_thumbnail(ID,youtube)
            print("UPDATING TITLE, go to https://www.youtube.com/watch?v=" + ID + " to check it out")
            timeout = 300
        else: 
            print("DID NOT UPDATE TITLE, will check again in " + str(timeout) + " seconds")
            timeout = 120
        print("current_views = " + str(current_views)) 
        print("viewcount = " + str(viewcount))
        viewcount = current_views
        likes = statistics[1]
        dislikes = statistics[2]
        comments = statistics[3]
        time.sleep(timeout)

            
if __name__ == "__main__":
    main()


