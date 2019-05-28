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
        return self.__extract_data()

    """Extrae los datos obviando las cabeceras"""
    def __extract_data(self):
        #TODO Mejor devolver un dict que una lista, procesarlo para hacerlos dict
        return self.raw_data._cell_values

    def __delete_headers(self):
        for index in range(0, self.count_headers_rows):
            self.raw_data._cell_values.pop(0)
        return self.raw_data
