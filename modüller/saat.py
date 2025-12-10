def saatmenü():
    print("╔══════════════════════════════════╗")
    print("║               SAAT               ║")
    print("╠══════════════════════════════════╣")
    print("║   1-Saat                         ║")
    print("║   2-Zamanlayıcı                  ║")
    print("║   3-Kronometre                   ║")
    print("║   4-Tarih                        ║")
    print("║   5-Anamenü                      ║")
    print("║                                  ║")
    print("║         Seçiminiz nedir?         ║")
    print("╚══════════════════════════════════╝")   
    seçim=input()
    
    if seçim=="1":
        import modüller.saat_canlısaat
        modüller.saat_canlısaat.canlısaatmenü()    
    if seçim=="2":
        import modüller.saat_zamanlayıcı
        modüller.saat_zamanlayıcı.zamanlayıcımenü()
    if seçim=="3":
        import modüller.saat_kronometre
        modüller.saat_kronometre.kronometremenü()
    if seçim=="4":
        import modüller.saat_tarih
        modüller.saat_tarih.tarihmenü()
    if seçim=="5":pass