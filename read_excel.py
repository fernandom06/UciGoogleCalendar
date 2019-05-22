from xlrd import open_workbook

class OpenData:
    def __init__(self, filename):
        self.filename = filename

    def open_excel(self):
        return open_workbook(filename=self.filename).sheet_by_index(0)

    def process_data(self):
        raw_data = self.open_excel()
        self.__extract_data()

    """Extrae los datos obviando las cabeceras"""
    def __extract_data(self):
        pass

