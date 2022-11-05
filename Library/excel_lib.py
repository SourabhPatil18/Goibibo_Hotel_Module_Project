import xlrd
from Library.configuration import Configuration


class ReadExcel:

    def read_test_data(self, sheetname):
        wb = xlrd.open_workbook(Configuration.TESTDATA_PATH)
        ws = wb.sheet_by_name(sheetname)
        columns = ws.ncols
        rows = ws.get_rows()
        header = next(rows)
        data = []

        for row in rows:
            if columns == 1:
                data.append(row[0].value)
            else:
                values = ()
                for j in range(columns):
                    values += (row[j].value,)
                data.append(values)
        return data

    def read_locator(self, sheetname):
        wb = xlrd.open_workbook(Configuration.LOCATORS_PATH)
        ws = wb.sheet_by_name(sheetname)
        rows = ws.get_rows()
        header = next(rows)
        dict_1 = {}
        for row in rows:
            dict_1[row[0].value] = (row[1].value, row[2].value)
        return dict_1

# rb = ReadExcel()
# print(rb.read_test_data("Hotel_Module_Data"))
