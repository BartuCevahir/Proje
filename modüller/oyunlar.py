def oyunlarmenü():
    print("╔══════════════════════════════════╗")
    print("║             OYUNLAR              ║")
    print("╠══════════════════════════════════╣")
    print("║   1-Taş Kağıt Makas              ║")
    print("║   2-Number Guess                 ║")
    print("║   3-Adam Asmaca                  ║")
    print("║   4-Hızlı Matematik              ║")
    print("║   5-Hızlı Yazma                  ║")
    print("║   6-Kart Oyunu                   ║")
    print("║   7-Karışık Kelime               ║")
    print("║   8-Anamenü                      ║")
    print("║                                  ║")
    print("║         Seçiminiz nedir?         ║")
    print("╚══════════════════════════════════╝")
    seçim=input()

    if seçim=="1":
        import modüller.oyunlar_taskagıtmakas
        modüller.oyunlar_taskagıtmakas.taskağıtmakasmenü()
    if seçim=="2":
        import modüller.oyunlar_sayıtahmini
        modüller.oyunlar_sayıtahmini.sayıtahminimenü()
    if seçim=="3":
        import modüller.oyunlar_adamasmaca
        modüller.oyunlar_adamasmaca.adamasmacamenü()
    if seçim=="4":
        import modüller.oyunlar_matematik
        modüller.oyunlar_matematik.matematikmenü()
    if seçim=="5":
        import modüller.oyunlar_hızlıyazma
        modüller.oyunlar_hızlıyazma.hızlıyazmamenü()
    if seçim=="6":
        import modüller.oyunlar_kartoyunu
        modüller.oyunlar_kartoyunu.kartoyunumenü()
    if seçim=="7":
        import modüller.oyunlar_karışıkkelime
        modüller.oyunlar_karışıkkelime.karışıkkelimemenü()

    if seçim=="8":pass