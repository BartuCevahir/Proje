def hesaplamalarmenü():
    print("╔══════════════════════════════════╗")
    print("║          HESAPLAMALAR            ║")
    print("╠══════════════════════════════════╣")
    print("║   1-Toplama                      ║")
    print("║   2-Çıkarma                      ║")
    print("║   3-Çarpma                       ║")
    print("║   4-Bölme                        ║")
    print("║   5-Üst Alma                     ║")
    print("║   6-Çarpım Tablosu               ║")
    print("║   7-Dikdörtgen Alanı             ║")
    print("║   8-Dikdörtgen Çevresi           ║")
    print("║   9-Anamenü                      ║")
    print("║  10-Çıkış                        ║")
    print("║                                  ║")
    print("║         Seçiminiz nedir?         ║")
    print("╚══════════════════════════════════╝")
    seçim=input()
    
    if seçim=="1":
        import modüller.hesaplamalar_toplama
        modüller.hesaplamalar_toplama.toplamamenü()
    if seçim=="2":
        import modüller.hesaplamalar_cıkarma
        modüller.hesaplamalar_cıkarma.cıkarmamenü()
    if seçim=="3":
        import modüller.hesaplamalar_carpma
        modüller.hesaplamalar_carpma.carpmamenü()
    if seçim=="4":
        import modüller.hesaplamalar_bolme
        modüller.hesaplamalar_bolme.bolmemenü()
    if seçim=="5":
        import modüller.hesaplamalar_ustalma
        modüller.hesaplamalar_ustalma.ustalamenü()
    if seçim=="6":
        import modüller.hesaplama_çarpımtablosu
        modüller.hesaplama_çarpımtablosu.carpımtablosumenü()
    if seçim=="7":
        import modüller.hesaplamalar_dikdörtgenalanı
        modüller.hesaplamalar_dikdörtgenalanı.dikdörtgenalanımenü()
    if seçim=="8":
        import modüller.hesaplamalar_dikdörtgencevresi
        modüller.hesaplamalar_dikdörtgencevresi.dikdörtgencevresimenü()

    if seçim=="9":
    if seçim=="10":pass