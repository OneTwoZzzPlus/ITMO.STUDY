import pandas as pd

excelDataDF = pd.read_excel('vegetable.xlsx', sheet_name='summer')

print(excelDataDF)
