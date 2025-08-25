from spellchecker import SpellChecker   # importing spellchecker library

spell = SpellChecker()   # create a SpellChecker object

t = 1
while t:
    a = input("Enter the word to be checked: ")	 # incorrect spelling
    print("Original text: " + str(a))     # printing original text

    # Find the most likely correction
    corrected_word = spell.correction(a)

    # prints the corrected spelling
    print("Corrected text: " + str(corrected_word))

    try:
        t = int(input("Try Again? 1 : 0 "))
    except:
        print("Exiting")
        t = 0
