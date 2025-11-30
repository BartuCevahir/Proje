def anamenü():
    print("╔══════════════════════════════════╗")
    print("║             PROJE1               ║")
    print("╠══════════════════════════════════╣")
    print("║   1- Hesaplamalar                ║")
    print("║   2- Çizimler                    ║")
    print("║   3- Oyunlar                     ║")
    print("║   4- Bilgi Yarışması             ║")
    print("║   5- Zamanlayıcı                 ║")
    print("║   6- Sözlük                      ║")
    print("║   7-                             ║")
    print("║   8-                             ║")
    print("║   9-                             ║")
    print("║  10-                             ║")
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
    anamenü()

       
anamenü()
