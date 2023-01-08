while True:
    print("***********************************")
    girdi = int(input("ussunu hesaplamak istediginiz sayiyi girin = "))
    us = int(input("girdiginiz sayinin ussunu yazin = "))
    i = 0
    sonuc = 1
    while i < us:
        sonuc = sonuc * girdi
        i+=1
    print("SONUC = ",sonuc)