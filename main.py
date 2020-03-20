import venv.package.modul_1 as md
import os


# Открытие файла из корневой папки программы с заменой разделительной черты
path = os.getcwd()+'\example.xlsx'
path.replace('\\', '/')

# создаем класс открытия файлов
prepare_data = md.OpenFileExel()
prepare_data.open_file(path,0)
print(prepare_data.data)



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



