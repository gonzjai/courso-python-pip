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

  
  
if __name__ == '__main__':
  print('hola')