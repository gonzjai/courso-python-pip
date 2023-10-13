import matplotlib.pyplot as plt

def generate_bar_chart(labels,values):
  fig, ax = plt.subplots()
  ax.bar(labels,values)
  #plt.title('Bar Chart')
  plt.savefig('bar.png')
  plt.close()

def generate_pie_chart(labels,values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  plt.title('Pie Chart')
  plt.savefig('pie.png')
  plt.close()

  

if __name__ == '__main__':
  print('hola')
  '''
  labels = read_csv.label
  values = read_csv.values
  labels.reverse()
  values.reverse()
  print(labels)
  print(values)
  generate_bar_chart(labels,values)
  
 # generate_pie_chart(labels,values)
 '''