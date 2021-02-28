import ftplib
import os

SERVER = 'uncle-**.com'
PORT = 2002
USER = 'test@uncle-**.com'
PASSWORD = ""

ftp = ftplib.FTP()
ftp.connect(SERVER,PORT)
ftp.login(USER,PASSWORD)

servpath = '/testcopyfile/stayu'

ftp.cwd(servpath) # accessed to servpath

print('BEFORE: ', ftp.nlst()) # fn.to dir file
print('=================')

path = r'C:\FTP_Work\Desktop'
allfile = os.listdir(path)
for f in allfile: # get file name in for loop
	if f[-3:] == 'txt':
		pathf = os.path.join(path,f)
		fileupload = open(pathf, 'rb')
		# result = ftp.storbinary('STOR ' + f, fileupload)
		ftp.storbinary('STOR ' + f, fileupload)
		# storbinary('STOR ' + save filename, open file from)
		# print('RESULT: ', result) # RESULT:  226 Transfer complete
		print('AFTER: ', ftp.nlst())
		print('-------')

ftp.quit()
