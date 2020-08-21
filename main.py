from pip._vendor.distlib.compat import raw_input


def anagramSolver(literki, slowo):
    for litera in slowo:
        if litera in literki:
            literki = literki.replace(litera, ' ',1)
        else:
            return 0
    return 1

letters = raw_input("Podaj anagram: ")

file = open('bin/slowa.txt','r')
for line in file:
    line = line.strip()
    if anagramSolver(letters,line):
        print(line)
file.close()