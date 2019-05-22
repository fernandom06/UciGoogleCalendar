from xlrd import open_workbook

class OpenData:
    def __init__(self, filename):
        self.filename = filename

    def open_excel(self):
        return open_workbook(filename=self.filename)

