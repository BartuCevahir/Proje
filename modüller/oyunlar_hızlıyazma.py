def hızlıyazmamenü():

    import time
    import random

    SENTENCES = [
        "python çok eğlenceli",
        "kod yazmayı seviyorum",
        "hızlı klavye pratik yap",
        "merhaba dünya",
        "yapay zeka gelecektir"
    ]

    def play():
        print("=== Typing Speed ===")
        score = 0
        rounds = 5
        for i in range(rounds):
            text = random.choice(SENTENCES)
            print("\nMetin:", text)
            input("Hazırsa Enter'a bas ve yazmaya başla...")
            t0 = time.time()
            typed = input()
            t = time.time() - t0
            correct_chars = sum(1 for a,b in zip(text, typed) if a==b)
            accuracy = correct_chars / max(1, len(text))
            gained = int(len(text.split()) * accuracy * max(1, 10 - t//1))
            score += gained
            print(f"Doğruluk: {accuracy*100:.1f}%, süre: {t:.2f}s, +{gained} puan. Toplam: {score}")
        print("Bitti! Toplam puan:", score)

    if __name__ == "__main__":
        play()
