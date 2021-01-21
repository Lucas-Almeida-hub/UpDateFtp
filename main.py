import FtpMode


class Controle:

    def switch(self, dayOfWeek):
        default = "Incorrect day"
        self.regisDados=['/debian/','ftp.us.debian.org','lucas','lds']
        print(self.regisDados)
        self.redeFtp = FtpMode.Conect(self.regisDados)
        return getattr(self, 'case_' + str(dayOfWeek), lambda: default)()
   
         
    def case_1(self):
        return(self.redeFtp)

    def case_2(self):
        return(self.redeFtp.readDir())
 
    def case_3(self): 
        return(self.redeFtp.moveDir())
    
    def case_4(self):
        return(self.redeFtp.dowlDir())




while (1):

    print(Controle().switch(input('\nDigite o valor referente a requesiçao\n 1-Conexao atual\n 2-Ler diretorio atual \n 3-Mover para outro diretorio \n 4-Abaixar arquivo de diretorio \n:')))
   










