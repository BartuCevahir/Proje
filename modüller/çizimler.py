def çizimlermenü():
    print("╔══════════════════════════════════╗")
    print("║             ÇİZİMLER             ║")
    print("╠══════════════════════════════════╣")
    print("║   1-Kare Çizimi                  ║")
    print("║   2-Üçgen Çizimi                 ║")
    print("║   3-Beşgen Çizimi                ║")
    print("║   4-Altıgen Çizimi               ║")
    print("║   5-Sekizgen Çizimi              ║")
    print("║   6-Desen Çizimi                 ║")
    print("║   7-Rastgele Kareler             ║")
    print("║   8-Anamenü                      ║")
    print("║                                  ║")
    print("║         Seçiminiz nedir?         ║")
    print("╚══════════════════════════════════╝")   
    seçim=input()
    if seçim=="1":
        import modüller.cizim_kare
        modüller.cizim_kare.kareçizimimenü()    
    if seçim=="2":
        import modüller.cizim_ucgen
        modüller.cizim_ucgen.ucgencizimimenü()
    if seçim=="3":
        import modüller.cizim_besgen
        modüller.cizim_besgen.beşgençizimimenü()
    if seçim=="4":
        import modüller.cizim_altıgen
        modüller.cizim_altıgen.altıgençizimimenü()
    if seçim=="5":
        import modüller.cizim_sekizgen
        modüller.cizim_sekizgen.sekizgençizimimenü()
    if seçim=="6":
        import modüller.cizim_şekil
        modüller.cizim_şekil.sekilcizimmenü()
    if seçim=="7":
        import modüller.cizim_rastgelekareler
        modüller.cizim_rastgelekareler.rastgelekareler()

    if seçim=="8":pass   
            