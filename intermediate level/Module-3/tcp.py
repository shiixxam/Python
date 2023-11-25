from ftplib import FTP 

host = "videoftptut.bplaced.net"
user = "root"
password = "1234"


with FTP(host) as ftp:
    ftp.login(user=user,passwd=password)
    print(ftp.getwelcome())