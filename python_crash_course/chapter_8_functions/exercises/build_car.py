def build_car(make, model, **car_info):
    """Build a dictionary for the information about the car"""
    car_info['make'] = make
    car_info['model'] = model
    return car_info

new_car = build_car('honda', 'civic', color = 'black', sunroof = True)

print(new_car)