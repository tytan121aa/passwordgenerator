import glob
import os

NEW_EXTENSION =".bak"

filename = input("Podaj wzorzec pliku: ")
all_files = glob.glob(filename)

for filename in all_files:
    if "." in filename:
        tokens = filename.rsplit(".", maxsplit=1)
        name, extension = tokens
    else:
        name = filename
        extension = " "
    new_filename = name + NEW_EXTENSION
    os.rename(filename, new_filename)
    print(filename, "->" , new_filename)
