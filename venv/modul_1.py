import numpy as np
from sklearn.linear_model import LinearRegression
from openpyxl import load_workbook
#ElectricityForecast


class OpenFileExel(object):

    def __init__(self):
        """Constructor"""
        self.filelink = None # ссылка файла
        self.worksheets = None # вызвает страницу
        self.page = 0
        self.max_column = None # максимальное количество столбцов данных
        self.max_row = None # максимальное количество строк данных
        self.data = None


    def open_file(self, filelink, page):
        self.filelink = filelink
        wb = load_workbook(filelink)
        self.worksheets = wb.worksheets[page]
        self.max_column = self.worksheets.max_column
        self.max_row = self.worksheets.max_row
        self.data = np.zeros((self.max_column, self.max_row))

# создаем класс открытия файлов
open_data = OpenFileExel()
open_data.open_file('D:/example.xlsx',0)
print(open_data.data)



# max_column = worksheets.max_column
# max_row = worksheets.max_row
# data = np.zeros((max_column, max_row))
# for i in range(1, worksheets.max_column + 1):
#     for j in range(1, worksheets.max_row + 1):
#         value = worksheets.cell(row=j, column=i).value
#         if value == None:
#             continue
#         else:
#             data[i - 1][j - 1] = value
# print(data)
# y = data[0, :]
# y = np.array(y).reshape(-1, 1)
# x = data [1,:]
# x = np.data.de
# reg = LinearRegression() # создаем класс линейной регрессии
# reg.fit(y, x)
# print(reg.coef_)
# print(reg.intercept_)


# print(x)
# print(y)
