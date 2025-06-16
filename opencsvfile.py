dates = []
with open("Book1.csv","r")as f:
    for line in f:
        tokens = line.split(',')
        date = tokens[0]
        week = tokens[1]
        month = tokens[2]
        dates.append([date,week])
for elements in dates:
    if elements[0] == '11':
        print(elements[1])
print(dates)