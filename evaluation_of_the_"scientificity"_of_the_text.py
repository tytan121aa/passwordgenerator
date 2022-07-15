import string

SPECIAL_SINGS = string.punctuation

text = input("Podaj tekst:")

for punc in SPECIAL_SINGS:
    text =text.replace(punc, " ")

words = text.split()

counts = 0
for word in words:
    if word.isnumeric():
        counts += 1
scientificness = 100*counts/len(words)
print('Poziom "naukowości" tekstu: ', scientificness, "%")
