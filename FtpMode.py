import os
from  getpass import getpass
from ftplib import FTP

class Conect:

    def __init__(self,nomeDir,host,user,passowor):
      self.nomeDir=nomeDir
      self.host=host
      self.passowor=passowor

    def bebe (self):
        usuario=[]
        try:
          print("Conectando")
          conexao = FTP("ftp.debian.org")
          conexao.cwd(self.nomeDir)
          print("b")
          #conexao.connect('ftp.debian.org',21)
          conexao.login(*usuario)
          print(conexao.retrlines('LIST'))
          conexao.retrbinary('RETR'+file,local.write,1024)
          conexao.quit()
        except expression as identifier:
          print(identifier)
          pass
        

    
    