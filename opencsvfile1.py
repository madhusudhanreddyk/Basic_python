dates = {}
with open("Book1.csv","r") as f:
    for line in f:
        tokens = line.split(',')
        date= tokens[0]
        week = tokens[1]
        dates[date] = week
print(dates['6'])