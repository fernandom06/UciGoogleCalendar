import csv


class CreateCalendar:
    def __init__(self, raw_data):
        self.headers = ['Subject', 'Start Date', 'Start Time', 'End Date', 'End Time', 'All Day Event', 'Description',
                        'Location', 'Private']
        self.raw_data = raw_data

    def create_csv(self):
        with open('calendar.csv', 'w', newline='', encoding='utf-8') as csv_calendar:
            writer = csv.writer(csv_calendar, delimiter=',')
            writer.writerow(self.headers)
            for row in self.raw_data:
                subject = row[2]
                start_date = row[0]
                start_time = None
                end_date = row[1]
                end_time = None
                all_day_event = True
                description = 'Carrera: ' + row[0] + ', categoria: ' + row[7] + ', web: ' + row[9]
                location = row[4]
                private = False
                writer.writerow([subject, start_date, start_time, end_date, end_time, all_day_event, description, location, private])
