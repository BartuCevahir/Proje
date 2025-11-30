def carpımtablosumenü():
    
    print("Demek çarpım tablosunu öğrenmek istiyorsun.")
    print("İşte 1'den 10'a kadar tüm basamaklar.")


    for a in range(1,11):
        print(f"\nBasamak: {a}")
        for b in range(0,11):
            print(f"{a}x{b}={a*b}")