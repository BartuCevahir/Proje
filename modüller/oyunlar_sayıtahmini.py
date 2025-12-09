def sayıtahminimenü():
    
    import random

    def play():
        print("=== Number Guess ===")
        name = input("İsmin: ")
        score = 0
        while True:
            low, high = 1, 100
            secret = random.randint(low, high)
            tries = 0
            print(f"\n{ name }, 1-100 arasında bir sayı tuttum. Tahmin et!")
            while True:
                guess = input("Tahmin (çıkmak için q): ")
                if guess.lower() == 'q':
                    print("Oyundan çıkılıyor.")
                    return
                if not guess.isdigit():
                    print("Sadece sayı gir.")
                    continue
                guess = int(guess)
                tries += 1
                if guess < secret:
                    print("Daha yüksek.")
                elif guess > secret:
                    print("Daha düşük.")
                else:
                    gained = max(10, 50 - tries*5)  # 10..50 arası
                    score += gained
                    print(f"Tebrikler! {tries} denemede buldun. +{gained} puan. Toplam: {score}")
                    break
            again = input("Tekrar oyna? (e/h): ")
            if again.lower() != 'e':
                print("Oyun bitti. Toplam puanın:", score)
                break

    if __name__ == "__main__":
        play()