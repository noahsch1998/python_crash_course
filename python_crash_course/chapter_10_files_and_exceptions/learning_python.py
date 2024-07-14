from pathlib import Path

path = Path('text_files/learning_python.txt')
contents = path.read_text()
contents = contents.replace('Python', 'Java')
print(contents)

string = ''
for line in contents.splitlines():
    print(line)