from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/sqlservice.admin']
SERVICE_ACCOUNT_FILE = 'keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1OwQguwtoAYchFGIYC1Q3oLrtnxFG_HFATQnXRJ93JFg'

service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range="Intern Assignment for Data Analytics!A2:AP2602").execute()
#values = result.get('values', [])
print(result)

#write in sheet
WRITE_SPREADSHEET_ID = '1qYEdhyddLREsy_Of138BTt4mhHNSVC5R9yRmfVdnMvY'
request = service.spreadsheets().values().update(spreadsheetId=WRITE_SPREADSHEET_ID, range=range_, valueInputOption=value_input_option, body=value_range_body)
