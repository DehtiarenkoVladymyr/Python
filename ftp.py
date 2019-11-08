from ftplib import FTP


ftp = FTP('ftp.cse.buffalo.edu')
ftp.login()
ftp.cwd('')
data = ftp.retrlines('LIST')



print(data)