import openpyxl


class Sheet:
    def __init__(self):
        self.workbook = openpyxl.Workbook()
        self.sheet = self.workbook.active

    def __getitem__(self, item):
        return self.sheet[item].value

    def __setitem__(self, key, value):
        self.sheet[key] = value

    def save(self):
        self.workbook.save('output.xlsx')
