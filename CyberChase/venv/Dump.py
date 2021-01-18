import pickle
import os

path = f"C:/Users/{os.getlogin()}/Desktop/CyberChase"
os.chdir(path)

with open(f"{path}\\CyberData.chase", "r") as raw_file:
    read = raw_file.read()

output_file = open(f"{path}\\CyberData.chase", "wb")
pickle.dump(read, output_file)
