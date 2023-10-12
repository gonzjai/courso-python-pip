import matplotlib.pyplot as plt

def generate_bar_chart(country,labels,values):
  fig, ax = plt.subplots()
  ax.bar(labels,values)
  plt.title(f'Population From {country}')
  plt.savefig(f'./img/{country}.png',format='png')
  plt.close()
  

def generate_pie_chart(country,labels,values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  plt.title(f'Population From {country}')
  plt.savefig(f'./img/{country}.png',format='png')
  plt.close()

  

if __name__ == '__main__':
  print('hola')