def futbolmenü():    

    sorular = [
        "Kaç sarı kart bir kırmızı kart eder?",
        "Maç süresi kaç dakikadır?",
        "Bir galibiyet kaç puandır?",
        "Bir beraberlik kaç puandır?",
        "Rakip ceza sahası içinde yapılan faul sonucunu verilen cezaya ne denir?",
        "Futbol kaç kişiyle oynanır?",
        "Sahada kaç tane hakem vardır?",
        "1 yıldız almak için kaç şampiyonluk gerekir?",
        "Top sahanın uzun kenarlarından dışarı çıkarsa ne atışı kullanılır?",
        "Renkleri sarı ve laciver olan süper lig takımı hangisidir?"

    ]
    cevaplar = [
        "2",
        "90",
        "3",
        "1",
        "penaltı",
        "11",
        "4",
        "5",
        "taç",
        "fenerbahçe",

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
