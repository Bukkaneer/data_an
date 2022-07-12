import pandas as pd
import csv
"""
way = input('Show-me the way!\n')
table = pd.read_csv(f'{way}')
print(table)
print(table.columns)
"""

def load_on_pandas():
    with open("Unidades_da_Rede_Federal_de_EPCT.csv", 'r') as f:
        df = pd.read_csv(f, sep=",")
        print(df)

def load_as_csv():
    with open("Unidades_da_Rede_Federal_de_EPCT.csv", 'r') as f:
        leitor = csv.reader(f)

        for indice, linha in enumerate(leitor):
            print(linha)
            if indice > 5:
                break



if __name__ == '__main__':
    option = int(input(
        """
        Ler com pandas -> 1
        Ler com csv -> 2
        """))

    if option == 1:
        load_on_pandas()
        exit()
    load_as_csv()

