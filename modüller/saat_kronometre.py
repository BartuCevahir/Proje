def kronometremenü():

    import time
    import os

    def kronometre():
        saniye = 0
        while True:
            os.system("cls" if os.name == "nt" else "clear")
            print("Kronometre:", saniye, "saniye")
            time.sleep(1)
            saniye += 1

    kronometre()