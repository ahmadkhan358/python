def masterYoga(s):
    words = s.split() 
    wordsLen = len(words) - 1 

    newWord = ""

    for i in range (wordsLen, -1, -1):
        newWord += words[i] + " "

    return newWord


def masterYoga2(s):
    return ' '.join(s.split()[::-1])

print(masterYoga2("ahmad khan"))
