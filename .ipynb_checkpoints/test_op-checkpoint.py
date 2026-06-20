import pandas as pd
import tabulate
import openpyxl
SRC_FILE = "source_reports/Отчёт по проблемам NRFS_2026-06-20_13-44-03.xlsx"
STAGE_MAPPING = "mappings/stage_map.xlsx"
s_file = pd.read_excel(SRC_FILE)
sm_file = pd.read_excel(STAGE_MAPPING, sheet_name="stage_map", index_col=0,
						skiprows=1)
#print(s_file.head(30))

# Fill Down — заполняем вниз (forward fill)
sm_file.ffill()
print(sm_file.head(30))
#for index, row in sm_file.iterrows():
#	for col in sm_file.columns:
#		print(sm_file[row, col])
#	print("\n")

#sm_file.reset_index(drop=True, inplace=True)
with pd.option_context('display.max_rows', 100,
                     'display.max_columns', 50,
                     'display.precision', 3):
    print(sm_file)

print("\n\n# Количество NaN в каждом столбце\n")
print(sm_file.isna().sum())  # Количество NaN в каждом столбце
print("\n# Первые 20 строк для визуального осмотра\n")
print(sm_file.head(20))      # Первые 10 строк для визуального осмотра

# import tabulate
print(sm_file.to_markdown())

# Информация о типах данных
print("\nИнформация о DataFrame:")
print(sm_file.info())

print("\nПечать 1 столбца:")
print(sm_file[['Этап заявки СМР']])