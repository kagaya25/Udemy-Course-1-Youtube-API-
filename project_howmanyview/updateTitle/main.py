import google_auth_oauthlib.flow
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
def changeVideoTitle(id,views,youtube):
    title = "This Video Has " + views + " Views " +  " "
    desc = """This video is about how awesome APIs are. \n 
    How to get your API key and oauth2.0 key
    https://www.youtube.com/watch?v=SNZ8ihHCmnQ&list=PLtfRFndo6b7IqtlbVJhEjBqcWSpYfUCAl
    Youtube API VIDEO:
    https://www.youtube.com/watch?v=Qmxa70xbbgE&list=PLtfRFndo6b7Ln-wiAjPl04vMnDblbsukz
    """
    #CLIENT_SECRET_FILE = 'client_secret.json'
    #SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
    #flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
    #credentials = flow.run_console()
    #youtube = build('youtube', 'v3', credentials=credentials)
    
    request = youtube.videos().update(
        part="snippet", #,status
        body={
          "id": id,
          "snippet": {
            "categoryId": 27,
            # "defaultLanguage": "en",
            "description": desc,
             "tags": [
               "kagaya john","tom scott","tomscott","api","coding","application programming interface","data api"
             ],
            "title": title
          },
        }
    )
    response = request.execute()
    print(response)
    #https://www.youtube.com/watch?v=XO2fhnG61-Q 
    # The id is XO2fhnG61-Q
