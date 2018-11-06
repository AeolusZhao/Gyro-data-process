import csv
import matplotlib.pyplot as plt

x = []
y = []

with open( "log_0002.csv", 'r') as csvfile:
    csvfile.readline()
    dataReader = csv.reader(csvfile, delimiter=';')
    interestingrows=[row for idx, row in enumerate(dataReader) if idx in (28, 29, 30, 31, 33, 34, 35, 36, 37, 38, 39, 62)]
    for row in interestingrows:
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
