def adamasmacamenü():   

    import random

    WORDS = ["python","bilgisayar","yazilim","oyun","kodlama","matematik","istanbul","galaksi"]

    print("=== Adam Asmaca ===")
    score = 0
    while True:
        word = random.choice(WORDS)
        guessed = set()
        wrong = 6
        while wrong > 0 and set(word) - guessed:
            display = " ".join([c if c in guessed else "_" for c in word])
            print("\nKelime:", display, f"(hak: {wrong})")
            ch = input("Harf tahmin et (q çıkış): ").lower()
            if ch == 'q':
                print("Toplam puan:", score); return
            if len(ch) != 1 or not ch.isalpha():
                print("Tek harf gir.")
                continue
            if ch in guessed:
                print("Zaten tahmin ettin.")
                continue
            if ch in word:
                guessed.add(ch)
                print("Doğru!")
            else:
                wrong -= 1
                print("Yanlış!")
        if set(word) - guessed == set():
            gained = wrong * 5
            score += gained
            print(f"Tebrikler! Kelime: {word}. +{gained} puan. Toplam: {score}")
        else:
            print("Hakların bitti. Kelime:", word)
        if input("Tekrar? (e/h): ") != 'e':
            print("Oyun bitti. Toplam puan:", score); break

    if __name__ == "__main__":
        adamasmacamenü()