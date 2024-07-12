# Create a dictionary. This can be empty or include values.

alien_0 = {'color': 'green', 'points': 5}

# Add new information to the dictionary.

alien_0['x_position'] = 0
alien_0['y_position'] = 25
alien_0['speed'] = 'medium'

# Modify existing information in the dictionary.

alien_0['color'] = 'blue'

# Use keys within the dictionary to modify the value of other keys

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
elif alien_0['speed'] == 'fast':
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment

# Remove keys from dictionary permanantly using del statement

del(alien_0['points'])

# Use the get method to retrieve information from the dictionary
# This avoids an error if the desired key is not defined

color = alien_0.get('color', "No color assigned.")
points = alien_0.get('points', "No point value assigned.")

print(color)
print(points)