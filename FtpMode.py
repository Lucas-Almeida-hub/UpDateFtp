
import os
from  getpass import getpass
from ftplib import FTP
import json
conexao=""

class Conect:
    def __init__(self,nomeDir,host,user,passowor):
      self.nomeDir=nomeDir
      self.host = host
      self.passowor=passowor

    def NewConnection(self):
        try:
          print("Conectando")
          conexao = FTP(self.host)
          conexao.login()
          return(conexao)
        except (RuntimeError, TypeError, NameError):
          return (RuntimeError, TypeError, NameError)



    def readDir(self):
        try:
          print(conexao.retrlines('LIST'))
          conexao.quit()
        except:
          conexao.quit()
 
    def moveDir(self,dir):
        conexao.cwd(dir) 
        print(conexao.retrlines('LIST'))
        #conexao.quit()


         #conexao.retrbinary('RETR'+file,local.write,1024)