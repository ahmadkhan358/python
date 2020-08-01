def animalCrackers(s):
    words = s.split()

    if(words[0][0] == words[1][0]):
        return True
    else:
        return False


print(animalCrackers("Ahmad Aqib"))