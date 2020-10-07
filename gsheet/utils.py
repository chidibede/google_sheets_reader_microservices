import gspread
import settings
import json
from oauth2client.service_account import ServiceAccountCredentials
# import pandas as pd

google_private_key = json.loads(f'"{settings.GOOGLE_PRIVATE_KEY}"')

config = dict(
    type="service_account",
    project_id=settings.GOOGLE_PROJECT_ID,
    private_key=google_private_key,
    private_key_id=settings.GOOGLE_PRIVATE_KEY_ID,
    client_email=settings.GOOGLE_CLIENT_EMAIL,
    client_id=settings.GOOGLE_CLIENT_ID,
)

scopes = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_dict(config, scopes)
gc = gspread.authorize(credentials)


def read_gsheet(request_data):
    data = request_data
    url = data['url']
    excluded_sheets = data['excluded_sheets']
    spreadsheet = gc.open_by_url(url)
    sheets = spreadsheet.worksheets()

    all_sheets = [sheet.title for sheet in sheets]
   
    needed_sheets = [title for title in all_sheets if title not in excluded_sheets]
    gsheet_data = {}
 
    for title in needed_sheets:
        gsheet_data[title]=spreadsheet.worksheet(title).get_all_records()
    return(gsheet_data)

