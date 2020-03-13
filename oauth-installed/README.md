# Using OAuth Client 

_"installed" desktop application_

Authentication use Google OAuth 2.0 through
- [google-auth-httplib2](https://pypi.org/project/google-auth-httplib2/)
- [google-auth-oauthlib](https://pypi.org/project/google-auth-oauthlib/)

Within Google OAuth client credential creation, there are few possible authentication scenarios depends on client types:
- https://developers.google.com/identity/protocols/oauth2?hl=en_GB#scenarios

When creating OAuth client ID, choosing **Web Application** as application type, then `credentials.json` look like:
```
{
    "web": {
        "client_id": "1234567890-C8anmeqln99f21bse06p8h8coimo3hrn.apps.googleusercontent.com",
        "project_id": "my-project-1234567890",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_secret": "<scrape>"
    }
}
```

When creating OAuth client ID, choosing **Other** as application type, then `credentials.json` look like:
```
{
    "installed": {
        "client_id": "1234567890-9eedBhk7g2BcD2upso7pm3om8472d4se.apps.googleusercontent.com",
        "project_id": "my-project-1234567890",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_secret": "<scrape>",
        "redirect_uris": [
            "urn:ietf:wg:oauth:2.0:oob",
            "http://localhost"
        ]
    }
}
```

Since [quickstart.py](quickstart.py) will be running as a Desktop app, choose **Other** as application type for OAuth client credential.

Then, the rest is using Google Spreadsheets API:
- [google-api-python-client](https://github.com/googleapis/google-api-python-client)
