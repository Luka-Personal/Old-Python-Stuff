CODE = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ' ': '/' }
 
def convertToMorseCode():
    text = input("შეიყვანეთ მესიჯი, რომელიც უნდა დაიშიფროს. გაითვალისწინეთ დაიშიფრება მხოლოდ ინგლისური ანბანის ასოები და ციფრები: ").upper()
    encodedSentence = ""
    for character in text:
        try:
         encodedSentence += CODE[character] + " "
             
        except:
            print(f"\n არასწორია: '{character}' მხოლოდ ინგლისური ასოები და ციფრები!!")
            convertToMorseCode()
            break

        outF = open("encrypted.txt", "w")
        outF.writelines(encodedSentence)
        outF.close()

        with open('encrypted.txt', 'r') as f:
         contents = f.read()

        with open('encrypted.txt', 'w') as f:
         f.write(contents.replace('/', '\n'))
         f.close()


if __name__ == "__main__":
    convertToMorseCode()
    print("\n ფაილი დაშიფრული ტექსტით დაგენერირებულია.")