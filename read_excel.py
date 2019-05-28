from xlrd import open_workbook

class OpenData:
    def __init__(self, filename, count_headers_rows):
        self.filename = filename
        self.count_headers_rows = count_headers_rows
        self.raw_data = self.open_excel()

    def open_excel(self):
        return open_workbook(filename=self.filename).sheet_by_index(0)

    def process_data(self):
        self.__delete_headers()
        self.__extract_data()

    """Extrae los datos obviando las cabeceras"""
    def __extract_data(self):
        self.date_from = []
        self.date_to = []
        self.name = []
        self.venue = []
        self.country = []
        self.category = []
        self.calendar = []
        self.uci_class = []
        self.email = []
        self.web = []
        for row in self.raw_data._cell_values:
            self.date_from.append(row[0])
            self.date_to.append(row[1])
            self.name.append(row[2])
            self.venue.append(row[3])
            self.country.append(row[4])
            self.category.append(row[5])
            self.calendar.append(row[6])
            self.uci_class.append(row[7])
            self.email.append(row[8])
            self.web.append(row[9])



    def __delete_headers(self):
        for index in range(0, self.count_headers_rows):
            self.raw_data._cell_values.pop(0)
        return self.raw_data


