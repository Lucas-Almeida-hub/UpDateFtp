import FtpMode


def createNewConect():

     conectPeople=FtpMode.Conect('/debian/','ftp.us.debian.org','lucas','lds')
     return ("OK")
def readDir():
    return conectPeople.readDir()
def moveDir():
    return conectPeople.moveDir('/debian')
def dowlDir():
    return conectPeople.dowlDir('README.HTML')


class Controle:
    
    def switch(self, dayOfWeek):
        default = "Incorrect day"
        self.redeFtp = FtpMode.Conect('/debian/','ftp.us.debian.org','lucas','lds')
        return getattr(self, 'case_' + str(dayOfWeek), lambda: default)()

    #def redeFtp(self):
        # return FtpMode.Conect('/debian/','ftp.us.debian.org','lucas','lds')
         
    def case_1(self):
        return self.redeFtp

    def case_2(self):
        return self.redeFtp.readDir()
 
    def case_3(self):
        return self.redeFtp.moveDir('/debian')

    def case_4(self):
        return self.redeFtp.dowlDir()


#


while (1):

    print(Controle().switch(input('\nDigite o valor referente a requesiçao\n 1-Conexao atual\n 2-Ler diretorio atual \n 3-Mover para outro diretorio \n 4-Abaixar arquivo de diretorio \n:')))
   











