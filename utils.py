def get_population(country_dict):
    population_dict = {
        '2012': int(country_dict['Population']),
        '2013': int(country_dict['Population']),
        '2014': int(country_dict['Population']),
        '2015': int(country_dict['Population']),
        '2016': int(country_dict['Population']),
        '2017': int(country_dict['Population']),
        '2018': int(country_dict['Population']),
        '2019': int(country_dict['Population']),
        '2020': int(country_dict['Population']),
        '2021': int(country_dict['Population']),
        '2022': int(country_dict['Population'])
    }
    labels = population_dict.keys()
    values = population_dict.values()
    return labels, values

def population_by_country(data, country):
    result = list(filter(lambda item : item['Country'] == country, data))
    return result
