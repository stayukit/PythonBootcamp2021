import ftplib
import os

SERVER = 'uncle-**.com'
PORT = 2002
USER = 'test@uncle-**.com'
PASSWORD = ""

ftp = ftplib.FTP()
ftp.connect(SERVER,PORT)
ftp.login(USER,PASSWORD)

mypath = '/testcopyfile/stayu'

ftp.cwd(mypath) # accessed to mypath

path = r'C:\FTP_Work\Download'
allfile = os.listdir(path)

filename = 'test.txt'
topathfile = os.path.join(path,filename)
file = open(topathfile, 'wb').write # write

result = ftp.retrbinary('RETR '+ filename, file) # retrbinary(origin, write to)
print('RESULT: ', result)

ftp.quit()
