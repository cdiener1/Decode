def dic_words():
    with open('words1.txt') as word_file:
        valid_words = set(word_file.read().split())
    return valid_words

if "cat" in dic_words():
    print(True)

real_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

words = input("Please enter your text (numerically represented) with - between letters. \n" )

print("words = " + words)

words_string = words.split()

print("words_string = %s" % words_string)

numwords = len(words_string)

print("numwords = %s" % numwords)

for wordloop in range(numwords):
    letters_string = words_string[wordloop].split("-")
    numletters = len(letters_string)
    globals()['letters%s' % wordloop] = numletters
    for letterloop in range(numletters):
        globals()['word%s_%s' % (wordloop, letterloop)] = letters_string[letterloop]
    

print("This is the letter at the requested position: %s" % word1_2)

print("There are %s letters in your chosen word." % letters1)

try:
    word1_2
except NameError:
    print("well, it WASN'T defined after all!")
else:
    print("sure, it was defined.")


for looper in range (numwords):
    pass
