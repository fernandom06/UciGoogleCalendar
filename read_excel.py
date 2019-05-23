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
        pass

    def __delete_headers(self):
        print(self.raw_data.nrows)
        for index in range(0, self.count_headers_rows):
            self.raw_data._cell_values.pop(0)
        self.raw_data.nrows = len(self.raw_data._cell_values)
        print(self.raw_data.nrows)
        return self.raw_data


