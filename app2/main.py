import read_csv
import utils
import charts



def run():
  data = read_csv.readcsv('./data.csv')
  #3print(data)
  country = input('put a country => ').capitalize()
  country_dict = utils.search_country(data,country)
  print(country_dict)
  labels, values = utils.get_population(country_dict)
  charts.generate_bar_chart(country,labels,values)
  charts.generate_pie_chart(country,labels,values)
  
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
  print('hola')