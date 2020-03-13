# Using Service Account

This use Service Account as scenario outlined in:
- https://developers.google.com/identity/protocols/oauth2?hl=en_GB#serviceaccount

Refer the following for all possible **OAuth 2.0 Scopes for Google APIs**
- https://developers.google.com/identity/protocols/oauth2/scopes?hl=en_GB

### google-auth User Guide
- https://github.com/googleapis/google-auth-library-python
- https://googleapis.dev/python/google-auth/latest/user-guide.html

### sheetsapi.py

Similar to `quickstart.py`, just that, it uses service account through Spreadsheets API:
- [google-api-python-client](https://github.com/googleapis/google-api-python-client)

### driveapi.py

Using service account and Drive API (instead of Spreadsheets API) to download export CSV of the first sheet.

- https://developers.google.com/drive/api/v3/manage-downloads
- https://developers.google.com/drive/api/v3/ref-export-formats
- http://wescpy.blogspot.com/2016/07/exporting-google-sheet--as-csv.html

### Share the file with service account

Either case, you will need to Share the document/file with a service account email. Otherwise, the following exception raise.

```
python sheetsapi.py
Traceback (most recent call last):
  File "sheetsapi.py", line 23, in <module>
    main()
  File "sheetsapi.py", line 13, in main
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME).execute()
    ...
    raise HttpError(resp, content, uri=self.uri)
googleapiclient.errors.HttpError: <HttpError 403 when requesting https://sheets.googleapis.com/v4/spreadsheets/1csMMHQXyRj2dkVaIqqdg7ppF5K2mqHTm1AY_qVLGveg/values/Sheet1%21A2%3AE?alt=json returned "The caller does not have permission">
```

```
python driveapi.py
Traceback (most recent call last):
  File "driveapi.py", line 26, in <module>
    main()
  File "driveapi.py", line 21, in main
    status, done = downloader.next_chunk()
    ...
    raise HttpError(resp, content, uri=self._uri)
googleapiclient.errors.HttpError: <HttpError 404 when requesting https://www.googleapis.com/drive/v3/files/1csMMHQXyRj2dkVaIqqdg7ppF5K2mqHTm1AY_qVLGveg/export?mimeType=text%2Fcsv&alt=media returned "File not found: 1csMMHQXyRj2dkVaIqqdg7ppF5K2mqHTm1AY_qVLGveg.">
```
