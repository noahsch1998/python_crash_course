from pathlib import Path

path = Path('guest.txt')
guest_list = ''

print("\nWhen done adding guests enter 'done'")

while True:
    name = input("Enter guest's full name: ")
    if name == 'done':
        break
    else:
        guest_list += f"{name}\n"


path.write_text(guest_list)