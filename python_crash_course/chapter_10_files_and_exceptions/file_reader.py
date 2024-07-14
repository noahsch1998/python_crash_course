from pathlib import Path

# create a path to retrieve the text file
path = Path('text_files/pi_digits.txt')
contents = path.read_text()

# to split the contents into lines
pi_string = ''
for line in contents.splitlines():
    pi_string += line.lstrip()

print(pi_string)
print(len(pi_string))