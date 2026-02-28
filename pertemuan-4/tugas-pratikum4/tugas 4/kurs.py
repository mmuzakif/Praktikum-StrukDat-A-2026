from tabulate import tabulate

data = [
    ["USD",16.875],
    ["EUR",19.995],
    ["SGD",16.360],
    ["JPY",109]
    
]
header = ["kode","kurs"]

print(tabulate(data,headers = header,tablefmt="fancy_grid"))