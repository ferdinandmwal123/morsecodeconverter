from playsound import playsound
import time
import pyttsx3 as pyttsx

MORSE_DICTIONARY = {'A': '.-', 'B': '-...',
                    'C': '-.-.', 'D': '-..', 'E': '.',
                    'F': '..-.', 'G': '--.', 'H': '....',
                    'I': '..', 'J': '.---', 'K': '-.-',
                    'L': '.-..', 'M': '--', 'N': '-.',
                    'O': '---', 'P': '.--.', 'Q': '--.-',
                    'R': '.-.', 'S': '...', 'T': '-',
                    'U': '..-', 'V': '...-', 'W': '.--',
                    'X': '-..-', 'Y': '-.--', 'Z': '--..',
                    '1': '.----', '2': '..---', '3': '...--',
                    '4': '....-', '5': '.....', '6': '-....',
                    '7': '--...', '8': '---..', '9': '----.',
                    '0': '-----', ', ': '--..--', '.': '.-.-.-',
                    '?': '..--..', '/': '-..-.', '-': '-....-',
                    '(': '-.--.', ')': '-.--.-'}


def txt_to_morse():
    txt = input('Enter text to be converted to morse code')
    code = [MORSE_DICTIONARY[letter.upper()] + ''
            for letter in txt
            if letter.upper() in MORSE_DICTIONARY.keys()]
    morse = ''.join(code)
    print(morse)
    for key in morse:
        if key == '.':
            playsound('/PycharmProjects/morsecodetranslator/dit.wav')
        elif key == '-':
            playsound('/PyCharmProjects/morsecodetranslator/dah.wav')
        else:
            time.sleep(0.5)


def morse_to_text():
    txt = input('Enter morse code to be converted to text')
    code = [z for i in txt.split() for z, x in MORSE_DICTIONARY.items() if i == x]
    newtxt = ''.join(code)
    print(newtxt)
    engine = pyttsx.init()
    engine.say(newtxt)
    engine.runAndWait()


print('''\n1 - Convert Text to morsecode \n2- Convert morsecode to text \n3- Quit\n''')

while True:
    try:
        selection = int(input("What do you want to do ?"))
        if selection == 1:
            print(txt_to_morse())
            break
        elif selection == 2:
            print(morse_to_text())
            break
        elif selection == 3:
            print('Okay bye')
            break
        else:
            print('Wrong selection enter again')
    except:
        print('Wrong selection enter again')
