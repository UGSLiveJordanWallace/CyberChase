import os

encoding_characters = {
    "a": "(",
    "A": "+",
    "b": "_",
    "B": "&",
    "c": "|",
    "C": "{",
    "d": "}",
    "D": "*",
    "e": "]",
    "E": ".",
    "f": ":",
    "F": ";",
    "g": "-",
    "G": "=",
    "h": "~",
    "H": "!",
    "i": "/",
    "I": "[",
    "j": 1,
    "J": 2,
    "k": 3,
    "K": 4,
    "l": 5,
    "L": 6,
    "m": 7,
    "M": 8,
    "n": 9,
    "N": "^",
    "o": "%",
    "O": "#",
    "p": "$",
    "P": "@",
    "q": "`",
    "Q": "<",
    "r": ">",
    "R": ",",
    "s": '"',
    " ": "þ",
    "S": "'",
    "t": "x",
    "T": "·",
    "u": "w",
    "U": "\\",
    "v": "¿",
    "V": "¡",
    "w": "é",
    "W": "€",
    "x": "┐",
    "X": "♂",
    "y": "‡",
    "Y": "¥",
    "z": "¢",
    "Z": "▓",
    ".": "∩",
    ",": "¸",
    "!": "µ",
    "?": "≈",
    "=": "»",
    "@": "╣"
}

path = f'C:\\Users\\{os.getlogin()}\\Desktop\\CyberChase'
os.chdir(path)
os.system(f"{path}\\CyberData.chase")
with open(f"{path}\\CyberData.chase", "r") as raw_file:
    message = raw_file.read()

empty = ''
for m in message:
    for i, encode in encoding_characters.items():
        if m == i:
            empty += f"{encode}"

with open(f"{path}\\CyberData.chase", "w") as encode_file:
    encode_file.write(empty)

os.system(f"{path}\\CyberData.chase")
