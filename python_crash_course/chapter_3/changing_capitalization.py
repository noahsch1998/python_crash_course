#Create name variables

first_name = "noah"
last_name = "schlottman"

#New variable for full name

full_name = f"{first_name} {last_name}"
print(full_name)

#Capitalize first and last name

full_name = f"{first_name.title()} {last_name.title()}"
print(full_name)

#All uppercase

full_name = full_name.upper()
print(full_name)

#All lowercase

full_name = full_name.lower()
print(full_name)

#Return to normal capitalization

full_name = full_name.title()
print(full_name)