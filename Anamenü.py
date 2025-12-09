def anamenü():
    print("╔══════════════════════════════════╗")
    print("║             PROJE1               ║")
    print("╠══════════════════════════════════╣")
    print("║   1- Hesaplamalar                ║")
    print("║   2- Çizimler                    ║")
    print("║   3- Oyunlar                     ║")
    print("║   4- Bilgi Yarışması             ║")
    print("║   5- Saat                        ║")
    print("║                                  ║")
    print("║         Seçiminiz nedir?         ║")
    print("╚══════════════════════════════════╝")

    seçim=input()
    if seçim=="1":
        import modüller.hesaplamalar
        modüller.hesaplamalar.hesaplamalarmenü()

    if seçim=="2":
        import modüller.çizimler
        modüller.çizimler.çizimlermenü()

    if seçim=="3":
        import modüller.oyunlar
        modüller.oyunlar.oyunlarmenü()

    if seçim=="4":
        import modüller.yarışma
        modüller.yarışma.yarışmamenü()
        
    if seçim=="5":
        import modüller.saat
        modüller.saat.saatmenü()
    anamenü()

       
anamenü()