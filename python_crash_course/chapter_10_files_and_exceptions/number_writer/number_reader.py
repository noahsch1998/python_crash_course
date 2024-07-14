from pathlib import Path
import json

path = Path('number_writer/numbers.json')
contents = path.read_text()
numbers = json.loads(contents)

print(numbers)