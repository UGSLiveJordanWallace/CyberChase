import os

decoding_characters = {
    "(" : "a",
    "+": "A",
    "_": "b",
    "&": "B",
    "|": "c",
    "{": "C",
    "}": "d",
    "*": "D",
    "]": "e",
    ".": "E",
    ":": "f",
    ";": "F",
    "-": "g",
    "=": "G",
    "~": "h",
    "!": "H",
    "/": "i",
    "[": "I",
    "1": "j",
    "2": "J",
    "3": "k",
    "4": "K",
    "5": "l",
    "6": "L",
    "7": "m",
    "8": "M",
    "9": "n",
    "^": "N",
    "%": "o",
    "#": "O",
    "$": "p",
    "@": "P",
    "`": "q",
    "<": "Q",
    ">": "r",
    ",": "R",
    '"': "s",
    "þ": " ",
    "'": 'S',
    "x": "t",
    "·": "T",
    "w": "u",
    "\\": "U",
    "¿": "v",
    "¡": "V",
    "é": "w",
    "€": "W",
    "┐": "x",
    "♂": "X",
    "‡": "y",
    "¥": "Y",
    "¢": "z",
    "▓": "Z",
    "∩": ".",
    "¸": ",",
    "µ": "!",
    "≈": "?",
    "»": "=",
    "╣": "@"
}

path = f'C:\\Users\\{os.getlogin()}\\Desktop\\CyberChase'
with open(f"{path}\\CyberData.chase", "r") as encodedFile:
    read = encodedFile.read()

emptystring = ''
for letter in read:
    for d, decode in decoding_characters.items():
        if letter == d:
            emptystring += decode

with open(f"{path}\\CyberData.chase", "w") as decode_file:
    decode_file.write(emptystring)

os.system(f"{path}\\CyberData.chase")