import pandas as pd

way = input('Show-me the way!\n')
table = pd.read_csv(f'{way}')
print(table)
print(table.columns)


