import sys
import xlwt
from datetime import datetime
import unittest

class TestExcel(unittest.TestCase):

    def test_simple_xls(self):
        style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on',
            num_format_str='#,##0.00')
        style1 = xlwt.easyxf(num_format_str='D-MMM-YY')

        wb = xlwt.Workbook()
        ws = wb.add_sheet('A Test Sheet')

        ws.write(0, 0, 1234.56, style0)
        ws.write(1, 0, datetime.now(), style1)
        ws.write(2, 0, 1)
        ws.write(2, 1, 1)
        ws.write(2, 2, xlwt.Formula("A3+B3"))

        wb.save('example.xls')

    def test_header_xls(self):
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Customers')

        # Sheet header, first row
        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = ['Nome', 'Sobrenome', 'E-mail', 'Nascimento', 'Criado em']

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        # Sheet body, remaining rows
        default_style = xlwt.XFStyle()
        wb.save('response.xls')


if __name__ == "__main__":
    unittest.main()