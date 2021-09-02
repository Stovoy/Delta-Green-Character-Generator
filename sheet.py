import openpyxl


class Sheet:
    def __init__(self):
        self.workbook = openpyxl.Workbook()
        self.sheet = self.workbook.active
        self.debug = False

    def __getitem__(self, key):
        # TODO: Debug logging
        if self.debug:
            print(f'[Debug] Get {key} ({self.sheet[key].value})')
        return self.sheet[key].value

    def __setitem__(self, key, value):
        # TODO: Debug logging
        if self.debug:
            print(f'[Debug] Set {key} = {value}')
        self.sheet[key] = value

    def save(self):
        self.workbook.save('output.xlsx')
