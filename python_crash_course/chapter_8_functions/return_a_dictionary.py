def profile(first, last, age = None):
    """return a dictionary of info about a person"""
    person = {'first': first, 'last': last}
    if age:
        person['age'] = age
    return person

person = profile('noah', 'schlottman', 26)
print(person)

person = profile('megan', 'larson')
print(person)