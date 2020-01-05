def dic_words(x):
    with open('words1.txt') as word_file:
        if "%s" % x in word_file.read().split():
            return True
        else:
            return False

a = "".join(['a','b','c','d'])


real_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

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

print("This is the letter at the requested position: %s" % word0_0)

print("There are %s letters in your chosen word." % letters0)

try:
    word0_1
except NameError:
    print("Undefined")
else:
    print("Defined.")



for loop in range(numwords):
    count = 0
    real_word = False
    while real_word == False:
        globals()['valid_word%s_%s' % (loop, loop)] = []
        for y in range(0, 26):
            try_word = ""
            count = count + 1
            for x in range(0, (globals()['letters%s' % (loop)])-1):
                globals()['test_word%s_%s' % (loop, x)] = real_letters[0]
                try_word = "".join([try_word, globals()['test_word%s_%s' % (loop, x)]])
            globals()['test_word%s_%s' % (loop, (globals()['letters%s' % (loop)]))] = real_letters[y]
            try_word = "".join([try_word, globals()['test_word%s_%s' % (loop, (globals()['letters%s' % (loop)]))]])
            if dic_words(try_word) == True:
                print(try_word)
                globals()['valid_word%s_%s' % (loop, loop)].append(try_word) #change second loop to z when made
                print(globals()['valid_word%s_%s' % (loop, loop)])
                real_word = True       
        real_word = True











              
