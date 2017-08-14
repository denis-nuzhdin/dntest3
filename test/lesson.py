from openpyxl import Workbook
import openpyxl
import datetime



wb = openpyxl.load_workbook("test.xlsx")
ws = wb.active

curent_time = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")

names = ['denis', 'alice','elena']

for name in names:
    ws.append([name] + [curent_time])

wb.save("test.xlsx")