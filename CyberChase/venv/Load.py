import pickle
import os

path = f"C:\\Users\\{os.getlogin()}\\Desktop\\CyberChase"
os.chdir(path)
input_file = open(f"{path}\\CyberData.chase", "rb")
var = pickle.load(input_file)
with open(f"{path}\\CyberData.chase", "w") as decoded_file:
    decoded_file.write(var)