from pathlib import Path

def show_file(file):
    path = Path(file)
    try:
        text = path.read_text()
    except FileNotFoundError:
        pass
    else:
        print(text)

filenames = ['cats.txt', 'dogs.txt', 'abc.txt']

for file in filenames:
    show_file(file)