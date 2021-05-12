import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xlrd
import openpyxl

# zadanie1
# tb = [1/x for x in range(1, 21)]
# tymcz = np.array(tb)
# plt.plot(tymcz)
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.axis([1, tymcz.size, 0, 1])
# plt.show()

# zadanie2
# tb = [1/x for x in range(1, 21)]
# tymcz = np.array(tb)
# plt.plot(tymcz, 'g^:', label="f(x)=1/x")
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.legend()
# plt.show()


# zadanie3
x = np.arange(0, 30, 0.1)
sn = np.sin(x)
cs = np.cos(x)
plt.plot(x, sn, 'c', label='f(x)=sin(x)')
plt.plot(x, cs, 'y', label='f(x)=cos(x)')
plt.yticks(np.arange(-1, 2, step=0.1))
plt.legend()
plt.show()

# zadanie4
# x = np.arange(0, 30, 0.1)
# f = np.sin(x)+2
# g = -(np.sin(x))
# plt.plot(x, f, x, g)
# plt.yticks(np.arange(-1, 3.5, step=0.5))
# plt.xlabel('x')
# plt.ylabel('sin(x)')
# plt.title('Wykres sin(x), sin(x)')
# plt.legend(['sin(x)', 'sin(x)'], loc='center left')
# plt.show()


# zadanie6
# excel = pd.ExcelFile('imiona.xlsx')
# df = pd.read_excel(excel, header=0)
# print(df)
#
# grup = df.groupby(['Plec']).agg({'Liczba':['sum']})
# wykres = grup.plot
# plt.ylabel("Liczba")
# plt.xticks(rotation=0)
# plt.show()