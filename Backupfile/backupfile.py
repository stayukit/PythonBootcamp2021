# save backupfile.py in path want to backup
import ftplib

SERVER = 'uncle-**.com'
PORT = 2002
USER = 'test@uncle-**.com'
PASSWORD = ""

ftp = ftplib.FTP()
ftp.connect(SERVER,PORT)
ftp.login(USER,PASSWORD)

servpath = '/testcopyfile/stayu'
ftp.cwd(servpath) # accessed to servpath

print('BEFORE: ', ftp.nlst()) # fn ftp.nlst() to dir file
print('=================')

filename = 'test - Copy.txt'

fileupload = open(filename, 'rb') # rb = read to binary
result = ftp.storbinary('STOR ' + filename, fileupload)
# storbinary('STOR ' + save filename, open from)
print('RESULT: ', result)
print('AFTER: ', ftp.nlst())

ftp.quit()
