from googleapiclient.discovery import build
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
SAMPLE_SPREADSHEET_ID = '1csMMHQXyRj2dkVaIqqdg7ppF5K2mqHTm1AY_qVLGveg'
SAMPLE_RANGE_NAME = 'Sheet1!A2:E'


def main():
    credentials = service_account.Credentials.from_service_account_file('local/credentials.json')
    service = build('sheets', 'v4', credentials=credentials.with_scopes(SCOPES))
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
    else:
        print(values)


if __name__ == '__main__':
    main()
