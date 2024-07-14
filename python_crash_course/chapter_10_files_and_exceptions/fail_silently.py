from pathlib import Path

def count_words(path):
    """Count the number of words in a file"""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
# the 'pass' statement tells Python to do nothing
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has {num_words} words.")

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']

for filename in filenames:
    path = Path(filename)
    count_words(path)