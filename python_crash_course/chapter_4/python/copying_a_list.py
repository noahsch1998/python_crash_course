# to copy a list you can create a slice of the entire list
# by omitting the first and last index in the slice

count = [num for num in range(1, 11)]
count_copy = count[:]
print(count_copy)