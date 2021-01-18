
import os
from  getpass import getpass
from ftplib import FTP
import json


class Conect:
    def __init__(self,nomeDir,host,user,passowor):
      self.nomeDir=nomeDir
      self.host = host
      self.passowor=passowor

    def __NewConnection(self):
        try:
          print("Conectando")
          conexao = FTP(self.host)
          conexao.login()
          return(conexao)
        except (RuntimeError, TypeError, NameError):
          return (RuntimeError, TypeError, NameError)



    def readDir(self):
        conexao=self.__NewConnection()
        return(conexao.retrlines('LIST'))#lista s arquivos do diretorio 
        conexao.quit()
      
    def moveDir(self,dir):
          self.dir =dir
          conexao=self.__NewConnection()
          conexao.cwd(self.dir)#caminhar ate o diretorio 
          return(conexao.retrlines('LIST'))
          conexao.quit()
    
    def dowlDir(self):
        conexao=self.__NewConnection()
        conexao.retrlines('LIST')
        print(self.dir)
        conexao.cwd(self.dir)
        print(conexao.retrlines('LIST'))
        with open('README', 'wb') as file:
          print(conexao.retrbinary('RETR README', file.write))
        conexao.quit()