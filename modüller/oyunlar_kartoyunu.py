def kartoyunumenü():
    
    import random

    def deal():
        return random.randint(1,11)

    print("=== Basit Blackjack ===")
    score = 0
    while True:
        player = deal() + deal()
        dealer = deal()
        print(f"Senin: {player}, Dealer: {dealer} (bir açık)")
        while True:
            move = input("Kart çek (c) / dur (d) / q ile çık: ")
            if move == 'q':
                print("Toplam puan:", score); return
            if move == 'c':
                player += deal()
                print("Toplamın:", player)
                if player > 21:
                    print("Bust! Kaybettin.")
                    break
            else:
                break
        if player > 21:
            score -= 5
            print("Puan -5. Toplam:", score)
        else:
            while dealer < 17:
                dealer += deal()
            print("Dealer:", dealer)
            if dealer > 21 or player > dealer:
                gained = 10
                score += gained
                print(f"Kazandın! +{gained}. Toplam: {score}")
            elif player == dealer:
                print("Berabere. Puan değişmedi.")
            else:
                score -= 5
                print(f"Kaybettin! -5. Toplam: {score}")
        if input("Tekrar? (e/h): ") != 'e':
            print("Oyun bitti. Toplam puan:", score); break

    if __name__ == "__main__":
        kartoyunumenü()