import statistics

stocks = {"info":[600,630,620],"ril":[1430,1490,1567],"mtl":[234,180,160]}

def print_all():
    for s,p in stocks.items():
        avg = statistics.mean(p)
        print(f'{s} ==>{p} ==> avg:',round(avg,2))


def add():
    stock_ticker = input("enter stock ticker")
    price = input("enter price of the stock ticker")
    price = float(price)
    if stock_ticker in stocks:
        stocks[stock_ticker].append(price)
    else:
        stocks[stock_ticker] = [price]
    print_all()

def main():
    op = input("enter operation like add printall")
    op = op.lower()
    if op == "add":
        add()
    elif op == "printall":
        print_all()
    else:
        print("invalid operator")

if __name__ == '__main__':
    main()
