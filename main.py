from read_excel import OpenData

FILENAME = 'data/Calendar_ROA_5_20_2019.xlsx'

raw_data = OpenData(filename=FILENAME, count_headers_rows=2).process_data()
print('minin')
