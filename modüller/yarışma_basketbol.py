def basketbolmenü():

    sorular = [
        "Basketbol kaç kişi ile oynanır?",
        "Serbest atış kaç puandır?",
        "Topu yere vurmadan koşmaya ne ad verilir?",
        "Atış kaçınca topa tekrardan sahip olmaya ne ad verilir?",
        "Avrupa liginin adı nedir?",
        "Bir çeyrek kaç dakikadır?",
        "Pota altında adımlama ile yapılan atışa ne ad verilir?",
        "Bir takımın bir sette kaç faul hakkı vardır?",
        "Euroleague'de en son şampiyon olan türk takımı kimdir?",
        "NBA'de bir çeyrek süresi ne kadardır?",

    ]
    cevaplar = [
        "5",
        "1",
        "steps",
        "ribaund",
        "euroleague",
        "10",
        "turnike",
        "4",
        "fenerbahçe",
        "12",

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
