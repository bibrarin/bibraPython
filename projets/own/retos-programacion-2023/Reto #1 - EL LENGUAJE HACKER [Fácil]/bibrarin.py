"""
 Escribe un programa que reciba un texto y transforme lenguaje natural a "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 se caracteriza por sustituir caracteres alfanuméricos.
 - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)  con el alfabeto y los números en "leet".
 """

def main():
    diccionario_hacker ={
        "a": "4",
        "b": "|3",
        "c": "[",
        "d": ")",
        "e": "3",
        "f": "|=",
        "g": "&",
        "h": "#",
        "i": "1",
        "j": ",_|",
        "k": ">|",
        "l": "1",
        "m": "mm",
        "n": "nn",
        "o": "0",
        "p": "|*",
        "q": "(_,)",
        "r": "I2",
        "s": "5",
        "t": "7",
        "u": "(_)",
        "v": "vv",
        "w": "ww",
        "x": "><",
        "y": "j",
        "z": "2",
        "0": "o",
        "1": "L",
        "2": "R",
        "3": "E",
        "4": "A",
        "5": "S",
        "6": "b",
        "7": "T",
        "8": "B",
        "9": "g",
    }

    while True:
        texto_final = ''
        texto_consola = input(">: ").lower()
        if (texto_consola == 'exit'):
            break

        for charact in texto_consola:
            texto_final += diccionario_hacker.get(charact,charact)

        print(texto_final)
main()