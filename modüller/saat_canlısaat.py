def canlısaatmenü():

    import time
    import os

    while True:
        os.system("cls" if os.name == "nt" else "clear")  
        current_time = time.strftime("%H:%M:%S")          
        print("Şu anki saat:", current_time)
        time.sleep(1)                                     