import ftplib
import os

SERVER = 'uncle-**.com'
PORT = 2002
USER = 'test@uncle-**.com'
PASSWORD = ""

ftp = ftplib.FTP()
ftp.connect(SERVER,PORT)
ftp.login(USER,PASSWORD)

accesspath = '/testcopyfile/stayu'
ftp.cwd(accesspath) # accessed to accesspath

print('BEFORE: ', ftp.nlst()) # ftp.nlst() to dir file
print('=================')

path = r'C:\FTP_Work\Download'
allfileserv = ftp.nlst()

for f in allfileserv:
	if f[-3:] == 'txt':
		topathfile = os.path.join(path,f)
		file = open(topathfile, 'wb').write
		result = ftp.retrbinary('RETR ' + f, file)
# retrbinary('RETR ' + filename from server, write to local)	
		print('RESULT: ', result)
		print('AFTER: ', ftp.nlst())
		print('-------')

ftp.quit()
