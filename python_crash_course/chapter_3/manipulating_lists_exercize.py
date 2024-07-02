guest_list = ['adrian peterson', 'randy moss', 'fran tarkenton']
print(f"{guest_list[0].title()}, {guest_list[1].title()}, and {guest_list[2].title()} are invited to dinner.")

popped_guest = guest_list.pop(0)
print(f"{popped_guest.title()} can not make it to dinner.")
guest_list.insert(0, 'justin jefferson')
print(f"{guest_list[0].title()} is invited to join in his place.")

print("We found a larger table.")
guest_list.append('jared allen')
guest_list.append('harrison smith')
guest_list.append('chad greenway')
print(f"{guest_list[3].title()}, {guest_list[4].title()}, and {guest_list[5].title()} are invited to join us.")