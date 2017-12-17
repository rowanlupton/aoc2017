# Advent of Code 2017 - Day 4: High-Entropy Passphrases

import csv

success = []
passphrases = csv.reader(open('4.txt'), delimiter="\n")

for passphrase in passphrases:
    phrases = list(csv.reader(passphrase, delimiter=" "))[0]
    phrases2 = phrases

    valid = True
    for index, phrase in enumerate(phrases):
        for phrase2 in phrases2[index+1:]:
            if sorted(phrase) == sorted(phrase2):
                valid = False
    if valid:
        success.append(passphrase)

print(len(success))
