population ={"china":143,"india":136,"usa":32,"pakistan":21}

def print_all():
    for country,p in population.items():
        print(f'{country}==>{p}')

def add():
    country = input("enter country name:")
    country = country.lower()
    if country in population:
        print(f'{country} is already exist in our database')
        return
    p = input(f'enter population of {country}:')
    population[country] = p
    print_all()

def remove():
    country = input("Enter country name:")
    country = country.lower()
    if country not in population:
        print(f"{country} doesn't exist in our database")
        return
    del population[country]
    print_all()

def query():
    country = input("Enter a country to query:")
    country = country.lower()
    if country not in population:
        print(f"{country} not exist")
        return
    print(f'the population of {country} is {population[country]}')


def main():
    op = input("Enter the operation like(add,remove,query,printall)")
    op = op.lower()
    if op == 'add':
        add()
    elif op == 'remove':
        remove()
    elif op == 'query':
        query()
    elif op == 'printall':
        print_all()
    else:
        print("invalid operation ")
if __name__ =='__main__':
    main()
