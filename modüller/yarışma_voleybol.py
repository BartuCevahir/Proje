def voleybolmenü():

    sorular = [
        "Voleybol kaç kişi ile oynanır?",
        "1 set kaçta biter?",
        "Maçı kaç set alan kazanır?",
        "Bir sette kaç oyuncu değişikliği hakkı vardır?",
        "Maçı kaç hakem takip eder?",
        "Voleybolda başlama vuruşuna ne denir?",
        "Voleybol topunu karşı sahaya geçirmek için kaç vuruş hakkın vardır?",
        "Oyuncuların yaptıkları yer değişikliğine ne ad verilir?",
        "Paslar ile oyun kuran oyuncuya ne ad verilir?",
        "Farklı renkte forma giyen oyuncuya ne ad verilir?",

    ]
    cevaplar = [
        "6",
        "25",
        "3",
        "6",
        "4",
        "servis",
        "3",
        "rotasyon",
        "pasör",
        "libero"

    ]




    sorulanlar =[]
    devam ="Evet"
    puan = 0
    import random, math
    while devam.lower() in ["evet","e","evt",""]:
        soruno = random.randint(0,len(sorular)-1)
        print("soruno:",soruno)
        if soruno not in sorulanlar:
            sorulanlar.append(soruno)
            cevap = input(sorular[soruno])
            if cevap.lower() == cevaplar[soruno].lower():
                puan += 100/len(sorular)
                print("bildin, puanın:", math.ceil(puan))
            
            else:
                print("bilemedin")
                puan -= 100/len(sorular)
                print("puanın:", math.ceil(puan))
        
            if len(sorulanlar)>=len(sorular): break
            else: devam=input("Devam etmek istiyor musun?\n(Devam için Evet yaz veya boş geç)")
    else: print(f"Yarışmayı{puan}puanıyla tamamladın.")
