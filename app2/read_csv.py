import csv

def readcsv(path):
  with open(path, 'r') as file:
    reader = csv.reader(file, delimiter=',')
    key = next(reader)
    finaltext = []
    for row in reader:
      iterable = zip(key,row)
      country_dict = {key: value for key, value in iterable}
      finaltext.append(country_dict)
    return finaltext
'''
def search_country(datacsv):
  country = input('digita un país => ').capitalize()
  for i in datacsv:
    if country in i['Country/Territory']:
      label = ['2022','2020','2015','2010','2000','1990','1980','1970']
      values = [i['2022 Population'],i['2020 Population'],i['2015 Population'],i['2010 Population'],i['2000 Population'],i['1990 Population'],i['1980 Population'],i['1970 Population']]
      for i in values:
        val.append(int(i))
      return label, values
finaltext = readcsv('./app/data.csv')
label, val = search_country(finaltext)
'''
  
  
if __name__ == '__main__':
  print('hola')
  
  




  
  '''
  print(finaltext) 
  position = 1
  for x in finaltext:
    print(position,' => ', x['Country/Territory'])
    position += 1
  print(len(finaltext))
  '''