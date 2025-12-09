def taskağıtmakasmenü():

    import random

    secenekler = ["taş", "kağıt", "makas"]

    cpu = random.choice(secenekler)
    sen = input("Taş, kağıt veya makas seç: ")

    print("Bilgisayar seçti:", cpu)

    if sen == cpu:
        print("Berabere!")
    elif (sen == "taş" and cpu == "makas") or (sen == "kağıt" and cpu == "taş") or (sen == "makas" and cpu == "kağıt"):
        print("Kazandın!")
    else:
        print("Kaybettin!")