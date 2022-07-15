password = input("podaj hasło:")
for char in password:
    if char.isalpha():
        type_ = "litera"
    elif char.isnumeric():
        type_ = "cyfra"
    elif char.isspace():
        type_ = "biały znak"
    else:
        type_ = "znak specjalny"
    print(char, type_)
