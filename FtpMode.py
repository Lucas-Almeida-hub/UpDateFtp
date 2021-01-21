
import os
from  getpass import getpass
from ftplib import FTP
import json


class Conect:


    def __NewConnection(self):
        try:
          print("Conectando")
          print(self.host)
          conexao = FTP(self.host)
          print(conexao)
          print(conexao.login())
          return(conexao)
        except (RuntimeError, TypeError, NameError):
          return (RuntimeError, TypeError, NameError)
          


    def readDir(self):
        return(self.conexao.retrlines('LIST'))#lista s arquivos do diretorio 

      
    def moveDir(self):
          self.conexao.cwd(self.nomeDir)#caminhar ate o diretorio 
          return(self.conexao.retrlines('LIST'))

    
    def dowlDir(self):
        self.conexao.cwd(self.nomeDir)
        print(self.conexao.retrlines('LIST'))
        with open('README', 'wb') as file:
          print(self.conexao.retrbinary('RETR README', file.write))
        
    
    def closseConect(self):
        self.conexao.quit()

    def __init__(self,dados=[]):
      print(dados[0])
      self.nomeDir=dados[0]
      self.host = dados[1]
      self.passowor=dados[2]
      self.conexao=self.__NewConnection()

    