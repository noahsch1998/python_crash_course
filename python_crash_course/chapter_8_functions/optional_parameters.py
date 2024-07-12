# to include optional arguments in a function
    # list them after mandatory arguments
    # give them an empty default value

def format_name(first, last, middle = ''):
    """Format a name from its three parts and return the name"""
    if middle:
        name = f"{first.title()} {middle.title()} {last.title()}"
    else:
        name = f"{first.title()} {last.title()}"
    return name

name = format_name('noah', 'schlottman', 'robert')
print(name)

name = format_name('megan', 'larson')
print(name)