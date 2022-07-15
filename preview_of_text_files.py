import glob

pattern = input("Podaj pattern: ")
filenames = glob.glob(pattern)
print("Zostaną wyświetlone następujace pliki: ")
for filename in filenames:
    print(filename)
acept = input("Czy chcesz wyświetlić pliki? (t/n):")
if acept == "t" or acept == "T": #if choice.lower() == "t"
    for filename in filenames:
        with open(filename, 'r') as stream:
            content = stream.read()
            lines = content.split('\n')
            first_line = lines[0]
        print(filename, ':', first_line)
else:
    print("Anulowano")
