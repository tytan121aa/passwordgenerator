text = input("Podaj tekst:")
anonymus_text = ""
for char in text:
    if char.isdigit():
        anonymus_text +="X"
    else:
        anonymus_text += char
print("Zanonimizowany tekst: ", anonymus_text)

# II version

for digit in "0123456789":
    text = text.replace(digit, "X") # konieczne przypisanie bo replace() zwraca kopie 
print("Rozwiązanie: ", text)
