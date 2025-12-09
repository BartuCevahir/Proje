def yarışmamenü():
    print("╔══════════════════════════════════╗")
    print("║             YARIŞMA              ║")
    print("╠══════════════════════════════════╣")
    print("║   1-Başkentler                   ║")
    print("║   2-Futbol                       ║")
    print("║   3-Basketbol                    ║")
    print("║   4-Voleybol                     ║")
    print("║                                  ║")
    print("║         Seçiminiz nedir?         ║")
    print("╚══════════════════════════════════╝")
    seçim=input()
    
    if seçim=="1":
        import modüller.yarışma_baskentler
        modüller.yarışma_baskentler.baskentlermenü()
    if seçim=="2":
        import modüller.yarışma_futbol
        modüller.yarışma_futbol.futbolmenü()
    if seçim=="3":
        import modüller.yarışma_basketbol
        modüller.yarışma_basketbol.basketbolmenü()
    if seçim=="4":
        import modüller.yarışma_voleybol
        modüller.yarışma_voleybol.voleybolmenü()
    