# Write a function that takes an array of words and smashes them together into
# a sentence and returns the sentence. You can ignore any need to sanitize words
# or add punctuation, but you should add spaces between each word. Be careful,
# there shouldn't be a space at the beginning or the end of the sentence!
#
list1 = ['g', 'd', 'd', 'g', 'a', 'gds']


# -------------------------------------


def smash1(words):
    return " ".join(words)


print(smash1(list1))


# -------------------------------------


def smash(words):
    i = 0
    length = len(words)
    str1 = ""
    while i < length:
        if i < length - 1:
            str1 += words[i] + " "
        else:
            str1 += words[i]
        i += 1

    return str1


print(smash(list1))

# --------------------------------------


smash3 = lambda x: ' '.join(x)

print(smash3(list1))


# -------------------------------------


def smash4(words):
    kalimat = ""
    for i in words:
        kalimat += i + " "

    return kalimat[:-1]


print(smash4(list1))
