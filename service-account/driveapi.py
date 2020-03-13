import io

from googleapiclient.http import MediaIoBaseDownload
from googleapiclient.discovery import build
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/drive.readonly']
SAMPLE_SPREADSHEET_ID = '1csMMHQXyRj2dkVaIqqdg7ppF5K2mqHTm1AY_qVLGveg'


def main():
    credentials = service_account.Credentials.from_service_account_file('local/credentials.json')
    service = build('drive', 'v3', credentials=credentials.with_scopes(SCOPES))
    request = service.files().export_media(fileId=SAMPLE_SPREADSHEET_ID, mimeType='text/csv')

    # fh = io.BytesIO()
    fh = io.FileIO('local/test.csv', mode='wb')
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print("Download %d%%." % int(status.progress() * 100))


if __name__ == '__main__':
    main()
