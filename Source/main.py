import csv
import matplotlib.pyplot as plt

x = []
y = []

with open( "log_0002.csv", 'r') as csvfile:
    csvfile.readline()
    dataReader = csv.reader(csvfile, delimiter=';')
    for row in dataReader:
        x.append(row[0])
        y.append(row[6])

plt.plot(x,y, label='Loaded from file!')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()

#x = []
#y = []

#with open('log_0002.csv','r') as csvfile:
#    kidFile = csvfile.readline()
#    plots = csv.reader(kidFile, delimiter=';')
#    for row in plots:
#        x.append(int(row[0]))
#        y.append(int(row[1]))

#plt.plot(x,y, label='Loaded from file!')
#plt.xlabel('x')
#plt.ylabel('y')
#plt.title('Interesting Graph\nCheck it out')
#plt.legend()
#plt.show()
