import csv

# do wyciagania kolumn z tabeli
def column(matrix, i):
    return [row[i] for row in matrix]

csvfile = open("data.csv", "r")

# delimiter okresla znak rozdzielajacy
csvread = csv.reader(csvfile, delimiter=',')

# wrzucenie wszystkich danych do tablicy
alldata = []
for row in csvread:
    alldata = alldata + [row]
    #print ', '.join(row)

csvfile.close()    
no_samples = len(alldata[0]) - 1
no_data = len(alldata) - 2

# wyciagamy nazwy pierwiastkow
names = column(alldata, 0)[2:]

# lecimy i tworzymy pliki w zadanym formacie

for i in range(1,no_data):
    data_column = column(alldata,i)
   
    filename = data_column[0] + '.dat' 
    f = open(filename, 'w')
    f.write(data_column[0] + '\n') #title
    f.write('   ' + data_column[1] + '\n') #gestosc
    f.write('        ' + str(no_data) + '\n') #ilosc danych
    
    for j in range(no_data):
        f.write(names[j] + '\n')
        f.write('   ' + data_column[j+2] + '  ' + '0.00000\n')
    
    f.close()

    