def zamanlayıcımenü():    

    import time
    import os

    def geri_sayim(saniye):
        while saniye > 0:
            os.system("cls" if os.name == "nt" else "clear")
            print("Zamanlayıcı:", saniye, "saniye kaldı")
            time.sleep(1)
            saniye -= 1

        os.system("cls" if os.name == "nt" else "clear")
        print("Süre doldu! 🔔")

    # ÖRNEK ÇALIŞTIRMA
    saniye = int(input("Kaç saniye geri saysın?: "))
    geri_sayim(saniye)