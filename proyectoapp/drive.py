from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

clave_API = AIzaSyBYX94F-Lu9iwxYhh0OFNYrmPD1CGVCY28

gauth = GoogleAuth()
gauth.LocalWebserverAuth() # Creates local webserver and auto handles authentication.
drive = GoogleDrive(gauth)

file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()

print('Files in the root folder:')
for file1 in file_list:
    print('title: %s, id: %s' % (file1['title'], file1['id']))

