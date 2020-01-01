def dic_words():
    with open('words1.txt') as word_file:
        valid_words = set(word_file.read().split())
    return valid_words

if "cat" in dic_words():
    print(True)
    
words = input("Please enter your text (numerically represented) with - between letters. \n" )

print(words)

words_string = words.split()

print(words_string)

numwords = len(words_string)

print(numwords)

for wordloop in range(numwords):
    letters_string = words_string[wordloop].split("-")
    numletters = len(letters_string)
    for letterloop in range(numletters):
        globals()['word%s_%s' % (wordloop, letterloop)] = letters_string[letterloop]
    

print(word1_2)

try:
    word1_2
except NameError:
    print("well, it WASN'T defined after all!")
else:
    print("sure, it was defined.")
