import FtpMode

conect1 = FtpMode.Conect('/debian/','ftp.us.debian.org','lucas','lds')
conect1.NewConnection()
print(conect1.readDir())
print(conect1.moveDir('debian'))



