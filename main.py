import sys
import re

def citire():
    #de la linia de comanda primim fisierele, apoi le citim
    file1 = sys.argv[1]
    file2 = sys.argv[2]

    f = open(file1, "r")
    g = open(file2, "r")

    global text1
    global text2
    text1 = f.read()
    text2 = g.read()

    #print(text1)
    #print(text2)

    f.close()
    g.close()

def propozitii(text):
    #impartim continului fisierelor in propozitii
    phrases=re.split('[?.!]',text)
    #print(phrases)

    phrasesUpdate=[]
    for prop in phrases:
        propUpdate = prop.replace('\n','')
        if propUpdate:
            phrasesUpdate.append(propUpdate)
    #print(phrasesUpdate)
    return phrasesUpdate

def cuvinte(prop):
    #impartim propozitiile in cuvinte
    wordsList=[]
    words = re.split('[ ]',prop)
    for word in words:
        if word:
                wordsList.append(word)
    #print(wordsList)
    return wordsList

if __name__ == '__main__':
    citire()

    p1 = propozitii(text1)
    p2 = propozitii(text2)

    totalWords1 = []
    for prop in p1:
        totalWords1.append(cuvinte(prop))
    #print(totalWords1)

    totalWords2 = []
    for prop in p2:
        totalWords2.append(cuvinte(prop))
    #print(totalWords2)

    #cautam propozitiile comune
    commonPhrases = []
    for prop1 in totalWords1:
        for prop2 in totalWords2:
            if prop1 == prop2:
                found = " ".join(prop1)
                if found not in commonPhrases:
                    commonPhrases.append(found)
    print(commonPhrases)

# Cîrjanu Andrei
