from pathlib import Path

path = Path('moby_dick.txt')
contents = path.read_text(encoding='utf-8')
words = contents.split()

print("When you are done searching enter 'quit search'")

while True:
    word = input("What word would you like to search for?: ")
    if word == 'quit search':
        break
    else:
        print(words.count(word))
