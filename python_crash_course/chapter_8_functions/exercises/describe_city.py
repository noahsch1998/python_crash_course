def describe_city(city, country='the united states'):
    print(f"\n{city.title()} is in {country.title()}.")

describe_city('new york')
describe_city('los angeles')
describe_city('toronto', 'canada')
describe_city('chicago')