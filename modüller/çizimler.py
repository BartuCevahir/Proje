def çizimlermenü():
    print("╔══════════════════════════════════╗")
    print("║             ÇİZİMLER             ║")
    print("╠══════════════════════════════════╣")
    print("║   1-Kare Çizimi                  ║")
    print("║   2-Üçgen Çizimi                 ║")
    print("║   3-Çokgen çizimi                ║")
    print("║   4-Desen Çizimi                 ║")
    print("║   5-                             ║")
    print("║   6-                             ║")
    print("║   7-                             ║")
    print("║   8-                             ║")
    print("║   9-                             ║")
    print("║  10-                             ║")
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
        
            