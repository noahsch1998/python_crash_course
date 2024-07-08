count = [num for num in range(1,11)]

# create a slice from the list "count"
print(count[2:6])

# print only the first thre numbers from count
print(count[:3])

# print only the last three numbers from count
print(count[7:])

# with an unknown list length you can still print only the last three numbers
print(count[-3:])