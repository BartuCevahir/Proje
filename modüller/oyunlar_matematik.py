def matematikmenü():

    import random
    import time

    # def play():
    print("=== Hızlı Matematik ===")
    score = 0
    rounds = 10
    for i in range(rounds):
        a = random.randint(1, 20)
        b = random.randint(1, 20)
        op = random.choice(['+','-','*'])
        expr = f"{a}{op}{b}"
        correct = eval(expr)
        print(f"Soru {i+1}/{rounds}: {expr} = ?")
        t0 = time.time()
        ans = input("Cevap: ")
        t = time.time() - t0
        if ans.strip() == str(correct):
            gained = 2 + max(0, int(3 - t))  # hızlı cevap bonusu
            score += gained
            print(f"Doğru! +{gained} puan (süre: {t:.2f}s). Toplam: {score}")
        else:
            score -= 1
            print(f"Yanlış. Doğru: {correct}. -1 puan. Toplam: {score}")
        print("Oyun bitti. Toplam puan:", score)

    if __name__ == "__main__":
        matematikmenü()