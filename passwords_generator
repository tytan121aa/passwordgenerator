n= input("Z ilu znaków ma się składać Twoje hasło:")
n_sign = int(n)
n_sign_lowercase = "".join(random.sample(string.ascii_lowercase, 10))
n_sign_uppercase = "".join(random.sample(string.ascii_uppercase, 10))
n_sign_digits = "".join(random.sample(string.digits, 10))
n_sign_punctuation = "" .join(random.sample(string.punctuation, 10))
passwords_generator = "".join(random.sample(n_sign_lowercase + n_sign_uppercase + n_sign_digits + n_sign_punctuation, n_sign))

if n_sign>7 and n_sign <21:
    print(passwords_generator)   
else:
    print("Wybrana liczba musi zawierać się w przedziale <8-20>")
