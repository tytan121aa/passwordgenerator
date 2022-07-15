password = input("Podaj swoje hasło: ")
announcement = password
lowercase = 0
uppercase = 0
space = 0
ssign = 0
character = 0


for char in announcement:
    character += 1
    if char.islower(): 
        # można ustawić np zmienną has_lowercase = True
        lowercase += 1
    elif char.isupper():
        uppercase += 1
    elif char.isdigit():
        continue
    elif char.isspace():
        space += 1
    else:
        ssign += 1

if lowercase >= 1 and uppercase >= 1 and ssign >=1 and space == 0:
    print("Twoje hasło jest bezpieczne")
else:
    print("Twoje hasło nie jest wystarczająco bezpieczne. Dostosuj się do poniższych reguł:") 
    if lowercase <1:
        print("- Twoje hasło musi zawierać małą literę")
    if uppercase <1:
        print("- Twoje hasło musi zawierać wielką literę")
    if space > 0:
        print("- Twoje hasło NIE może zawierać spacji")
    if ssign < 1: 
        print("- Twoje hasło musi zawierać znak specjalny")
    if character <= 7:
        print("- Twoje hasło musi składać się minimum z 8 znaków")
