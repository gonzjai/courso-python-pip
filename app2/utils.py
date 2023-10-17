def get_population(country_dict):
  population_country = {
    2022: int(country_dict['2022 Population']),
    2020: int(country_dict['2020 Population']),
    2015: int(country_dict['2015 Population']),
    2010: int(country_dict['2010 Population']),
    2000: int(country_dict['2000 Population']),
    1990: int(country_dict['1990 Population']),
    1980: int(country_dict['1980 Population']),
    1970: int(country_dict['1970 Population']),
  } 
  labels = population_country.keys()
  values = population_country.values()
  return labels, values 

def search_country(data, country):
  country_dict = list(filter(lambda i: i['Country/Territory'] == country, data))
  return country_dict

if __name__ == '__main__':
  print('hola')
  