import google_auth_oauthlib.flow
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.http import MediaFileUpload

def update_thumbnail(id,youtube):
    #CLIENT_SECRET_FILE = 'client_secret.json'
    #SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]
    #flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
    #credentials = flow.run_console()
    #youtube = build('youtube', 'v3', credentials=credentials)
    
    request =youtube.thumbnails().set(
    videoId=id,
    media_body=MediaFileUpload("./make_thumbnail/thumbnail.jpg")
    ).execute()
    response = request
    print(response)
    
    #https://www.youtube.com/watch?v=XO2fhnG61-Q 
    # The id is XO2fhnG61-Q
