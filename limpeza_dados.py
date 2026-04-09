import pandas as pd

df = pd.read_csv('Data.csv', encoding='utf-8', skipinitialspace=True)

colunas_uteis = ['Tags', 'Min', 'Pauses (min)', 'Start Hour', 'End Hour']

df.columns = df.columns.str.strip()

df = df[colunas_uteis]

df.to_csv('dadoslimpos.csv', index=False, encoding='utf-8')

print(df.head(50))