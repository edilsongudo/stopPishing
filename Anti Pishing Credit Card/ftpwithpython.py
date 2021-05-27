import ftplib
import os

server = '192.168.43.108'
username = 'generic_user'
password = 'password'
myFTP = ftplib.FTP(server, username, password)
myFTP.cwd('dev_hdd0/GAMES')
myPath = r'rdr'


def uploadThis(path):
    files = os.listdir(path)
    os.chdir(path)
    for f in files:
        if os.path.isfile(f):
            fh = open(f, 'rb')
            myFTP.storbinary('STOR %s' % f, fh)
            fh.close()
        elif os.path.isdir(f):
            myFTP.mkd(f)
            myFTP.cwd(f)
            uploadThis(f)
    myFTP.cwd('..')
    os.chdir('..')


uploadThis(myPath)
