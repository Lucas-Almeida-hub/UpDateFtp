from FtpMode import Conect 



class controle :

    
        rede=[5]*2
        regisDados=[4]*10
        regisDados[0]=['/debian/','ftp.us.debian.org','lucas','lds']
        regisDados[1]=['/debian/','ftp.us.debian.org','lucas','lds']
        regisDados[3]=['/debian/','ftp.us.debian.org','lucas','lds']
        regisDados[4]=['/debian/','ftp.us.debian.org','lucas','lds']
        regisDados[5]=['/debian/','ftp.us.debian.org','lucas','lds']
        regisDados[6]=['/debian/','ftp.us.debian.org','lucas','lds']


            
        def TesteRede(regisDados,rede):
            for x in range(0,2):
                print(x)
                print(regisDados[x])
                print(rede[x])
                rede[x]=Conect(regisDados[x])
                print(rede[x])
                rede[x].closseConect()
                print(rede[x])

        def BaixarArquvo(regisDados,rede):
            for x in range(0,1):
                print(x)
                print(regisDados[x])
                rede[x]=Conect(regisDados[x])
                print(rede[x])
                print(rede[x].readDir())
                print(rede[x])
                print(rede[x].moveDir())
                print(rede[x])
                print(rede[x].dowlDir(str(input('Digite arquivo que deseja realizar dowloods : '))))
                print(rede[x])
                print(rede[x].closseConect())

        Menu=(int(input("| Digiteo intem requesitado \n| 1-para testar conexao \n| 2-Para abaixar arquivo\n: ")))

        if(Menu==1):
            TesteRede(regisDados,rede)
        if(Menu==2):
            BaixarArquvo(regisDados,rede)
                    
        
