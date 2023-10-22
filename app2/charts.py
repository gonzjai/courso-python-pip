import matplotlib.pyplot as plt


def generate_bar_chart(Continent,labels,values):
  fig, ax = plt.subplots()
  ax.bar(labels,values)
  plt.title(f'Population Persentage From {Continent}')
  plt.savefig(f'./img/{Continent}bar_chart.png',format='png')
  plt.close()
  

def generate_pie_chart(Continent,labels,values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  plt.title(f'Population Persentage From {Continent}')
  plt.savefig(f'./img/{Continent}pie_chart.png',format='png')
  plt.close()

  

if __name__ == '__main__':
  print('hola')