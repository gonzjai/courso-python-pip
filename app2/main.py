import read_csv
import utils
import charts
import pandas as pd


def run():
  df = pd.read_csv('./data.csv')
  df = df[df['Continent'] == 'Africa']
  data = read_csv.readcsv('./data.csv')
  continent = 'Africa'
  countries = df['Country/Territory'].values
  percentages = df['World Population Percentage'].values

  charts.generate_bar_chart(continent,countries,percentages)
  charts.generate_pie_chart(continent,countries,percentages)
  
  '''#3print(data)
  country = input('put a country => ').capitalize()
  country_dict = utils.search_country(data,country)
  print(country_dict)
  labels, values = utils.get_population(country_dict)
  
  '''
'''
def run2()
  data = read_csv.readcsv('data.csv)
  labels, values  = utils.getb_colum(dat)
  labels = labe)
  values = valu)
  print(label)
  print(value)
  print(len(values))
charts.generate_pie_chart(labels,values)
charts.generate_bar_chart(labels,values)

def run3():
  data = read_csv.readcsv('data.csv')
  labels, values = utils.better_column(data)
  charts.generate_pie_chart(labels,values)
'''

run()

if __name__ == '__name__':
  run()