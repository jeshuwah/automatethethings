from ftplib import FTP
from shutil import copyfile
import os   
import fileinput
import time

# define variables
NetActiveFile = '[filename]'
NetActiveFilePath = '[file location]'
UploadFolder = '[upload folder path]'
DownloadFolder = '[download folder path]'
FTPLoc = '[FTP server ip/address]'
FTPPort = [FTP server port]
FTPLogin = '[FTP login]'
FTPPass = '[FTP password]'

# establish FTP connection
print("Logging into FTP server.")
ftp = FTP()
ftp.connect(FTPLoc, FTPPort)
ftp.login(FTPLogin, FTPPass)

# display the server welcome
print(ftp.getwelcome())

# move file to be uploaded to /upload
print("Moving " + NetActiveFile + " to /upload folder.")
try:
    copyfile(NetActiveFilePath + NetActiveFile, UploadFolder + NetActiveFile)
except:
    print("File copy not successful")

# delete NetActive file if present
print("Checking if " + NetActiveFile + " is present on FTP.")
try:
    ftp.delete(NetActiveFile)
except:
    print("File not present. Pushing forward.") 

# upload NetActive.txt to FTP
try:
    with open(UploadFolder + NetActiveFile, 'rb') as f:
      ftp.storbinary('STOR ' + NetActiveFile, f)
    print("File upload successful.")
except:
    print("File upload not successful.")

# let the file marinate for 30 seconds
print("Waiting a few seconds...")
time.sleep(30)

# download NetActive.txt from FTP
try:
    with open(DownloadFolder + NetActiveFile, 'wb') as f:
        ftp.retrbinary('RETR ' + NetActiveFile, f.write)
    print("File download successful.")
    time.sleep(5)
except:
    print("File download not successful.")


# clean up /upload and /download folders
try:
    os.remove(UploadFolder + NetActiveFile) # /upload
    os.remove(DownloadFolder + NetActiveFile) # /download
    print("Files cleaned up successfully.")
except:
    print("Files not cleaned up successfully.")

# log off the FTP
print("Logging off FTP...")
try:
    ftp.quit()
    time.sleep(3)
    print("FTP connection terminated")
except:
    print("Cannot log off FTP")