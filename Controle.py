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


            
        if(input("w")=='w'):
            for x in range(0,2):
                print(x)
                print(regisDados[x])
                print(rede[x])
                rede[x]=Conect(regisDados[x])
                print(rede[x])
                rede[x].closseConect()
                print(rede[x])

        if(input("q")=='q'):
            for x in range(0,1):
                print(x)
                print(regisDados[x])
                rede[x]=Conect(regisDados[x])
                print(rede[x])
                print(rede[x].readDir())
                print(rede[x])
                print(rede[x].moveDir())
                print(rede[x])
                print(rede[x].dowlDir(input('Digite arquivo que deseja realizar dowloods : ')))
                print(rede[x])
                print(rede[x].closseConect())
