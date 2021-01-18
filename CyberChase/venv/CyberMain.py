import os
import random
import time

path = f'C:\\Users\\{os.getlogin()}\\Desktop'
newFolder = 'CyberChase'
os.chdir(path)
try:
#################################################
    if not os.path.exists(newFolder):
        os.mkdir(newFolder)
        os.chdir(newFolder)
        os.system('cd.> CyberData.chase')
    else:
        os.rmdir(newFolder)
#################################################
except OSError:
    pass

message = "You have been hacked lol,                                                                                 " \
          "                                                                                                             " \
          "                                                                                                            " \
          "                                                                                                             "
encoding_characters = '934howieshfliug4u3vwcoru32oquadxpsydx2ye9r5e486rywip3hw4nofe023y89583-982038==-=-+/-Rem/*+.214``asmdlfh][][][{}{}{}-0(&%$^&%$#@@#$%%$#@!@#$%^&^%$#@!!!@@@!`~~~~~~~~'
new_message = ''
for m in message:
    new_message += f"{random.choice(encoding_characters)}"
with open(f'{path}\\CyberChase\\CyberData.chase', 'w') as file:
    file.write(f"{new_message}")