from function_city_country import format_city

def test_city_country():
    """Do names like Santiago, Chile work?"""
    formatted_city = format_city('santiago', 'chile')
    assert formatted_city == 'Santiago, Chile'

def test_city_country_population():
    """Do names like Santiago, Chile work with a population number?"""
    formatted_city = format_city('santiago', 'chile', 5_000_000)
    assert formatted_city == 'Santiago, Chile - Population: 5000000'