import read_csv
import utils
import charts
import pandas as pd


def run():
  df = pd.read_csv('./data.csv')
  continent = input('Type a Continent (Asia,Africa,North America,South America,Oceania) => ').title()
  df = df[df['Continent'] == continent]

  countries = df['Country/Territory'].values  #labels
  percentages = df['World Population Percentage'].values   #values

  charts.generate_bar_chart(continent,countries,percentages)
  charts.generate_pie_chart(continent,countries,percentages)
  
  '''
  data = read_csv.readcsv('./data.csv')
  #3print(data)
  country = input('put a country => ').capitalize()
  country_dict = utils.search_country(data,country)
  print(country_dict)
  labels, values = utils.get_population(country_dict)
  
  '''

#run()

if __name__ == '__main__':
  run()