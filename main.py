from read_excel import OpenData

FILENAME = 'data/Calendar_ROA_5_20_2019.xlsx'

raw_data = OpenData(filename=FILENAME).process_data()
print('minin')
