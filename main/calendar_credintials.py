import os.path
from google.oauth2 import service_account
from googleapiclient.discovery import build
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
calendar_link = "https://calendar.google.com/calendar/u/0/r/"
SCOPES = ["https://www.googleapis.com/auth/calendar"]


def authenticate_google_calendar():
    credentials = service_account.Credentials.from_service_account_file(os.path.join(BASE_DIR, "credintials.json"), scopes=SCOPES)
    return credentials

def get_google_calendar_service():
    creds = authenticate_google_calendar()
    return build("calendar", "v3", credentials=creds)