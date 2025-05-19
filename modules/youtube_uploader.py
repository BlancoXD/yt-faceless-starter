import os
import pickle
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

def upload_video(title, description, video_file, thumbnail_file, credentials_path):
    creds = None

    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES)
            creds = flow.run_local_server(port=0)
        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)

    youtube = build("youtube", "v3", credentials=creds)

    request_body = {
        "snippet": {
            "title": title,
            "description": description,
            "tags": ["AI", "YouTube Automation", "Faceless"],
            "categoryId": "22"
        },
        "status": {
            "privacyStatus": "private"
        }
    }

    media_file = MediaFileUpload(video_file, mimetype="video/*", resumable=True)
    response = youtube.videos().insert(
        part="snippet,status",
        body=request_body,
        media_body=media_file
    ).execute()

    if thumbnail_file:
        youtube.thumbnails().set(
            videoId=response["id"],
            media_body=thumbnail_file
        ).execute()

    print("Video uploaded:", response["id"])

from googleapiclient.http import MediaFileUpload
