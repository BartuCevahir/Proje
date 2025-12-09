def karışıkkelimemenü():
    
    import random, time

    WORDS = ["python","bilgisayar","programlama","oyun","kod","algoritma","fonksiyon"]

    def scramble(w):
        arr = list(w)
        random.shuffle(arr)
        return "".join(arr)

    def play():
        print("=== Word Scramble ===")
        score = 0
        rounds = 7
        for i in range(rounds):
            w = random.choice(WORDS)
            s = scramble(w)
            print(f"\nKarışık: {s}")
            t0 = time.time()
            ans = input("Tahmin: ").strip().lower()
            t = time.time() - t0
            if ans == w:
                gained = len(w) + max(0, int(5 - t))
                score += gained
                print(f"Doğru! +{gained}. Toplam: {score}")
            else:
                print("Yanlış. Doğru:", w)
        print("Bitti. Toplam puan:", score)

    if __name__ == "__main__":
        play()
