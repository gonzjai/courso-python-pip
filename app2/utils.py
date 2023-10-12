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
  for x in data:
    if x['Country/Territory'] == country:
      dict_country = x
  return dict_country

'''
def population_by_country(data,country):
  result = list(filter(lambda i: i['Country/Territory'] == country,data))
  return result

  

def getb_colum(data):
  country = []
  labels = []
  values = []
  for x in data:
    intToAdd = x['World Population Percentage']
    country = x['Country/Territory']
    labels.append(country)
    values.append(float(intToAdd))
  return labels, values


def better_column(data):
  continent = input('write a continent [Asia, Europe, Africa, Oceania, North America, South America] => ').title()
  dataFilt = list(filter(lambda x: x['Continent'] == continent,data))
  values = list(map(lambda x: float(x['World Population Percentage']),dataFilt))
  labels = list(map(lambda y: y['Country/Territory'], dataFilt))
  return  labels, values
'''

if __name__ == '__main__':
  print('hola')
  