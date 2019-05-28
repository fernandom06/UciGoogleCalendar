from read_excel import OpenData
from create_calendar import CreateCalendar

FILENAME = 'data/Calendar_ROA_5_20_2019.xlsx'

raw_data = OpenData(filename=FILENAME, count_headers_rows=2).process_data()
CreateCalendar(raw_data).create_csv()
