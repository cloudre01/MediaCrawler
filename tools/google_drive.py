from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload


class GoogleDriveUploader:
    def __init__(self, credentials_path):
        self.SCOPES = ["https://www.googleapis.com/auth/drive.file"]
        self.creds = self._get_credentials(credentials_path)
        self.service = build("drive", "v3", credentials=self.creds)

    async def upload_file(self, file_path, folder_id=None):
        file_metadata = {"name": file_path.split("/")[-1]}
        if folder_id:
            file_metadata["parents"] = [folder_id]

        media = MediaFileUpload(file_path)
        file = (
            self.service.files()
            .create(body=file_metadata, media_body=media, fields="id")
            .execute()
        )
        return file.get("id")
