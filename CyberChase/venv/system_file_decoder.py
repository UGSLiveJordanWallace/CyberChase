import os
import pickle
import time
import threading

path = f"C:\\Users\\{os.getlogin()}\\Desktop\\CyberChase"
try:
    if not os.path.exists(path):
        print("Path just make the folder \"CyberChase\"")
    else:
        print("CyberChase decoder is in >")
        print("Getting file...")
        threading.Thread(time.sleep(3)).start()
        print("Reformating file...")
        threading.Thread(time.sleep(6)).start()
        print("Retrieving code...")
        threading.Thread(time.sleep(12)).start()
        print("Decoding ChaseEncryption...")
        threading.Thread(time.sleep(3)).start()
        print("Getting Message...")
        with open(f"{path}\\CyberData.chase", "w") as file:
            read = file.write("You have been hacked lol")
        print("Decryption Successful")
        os.system(f"{path}\\CyberData.chase")
except OSError:
    pass