import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime as datetime
#----------------------Ввод массива данных из локального файла '.xlsx'-------------------------#
df = pd.read_excel(r"D:\Данные\МУИВ\2 курс\Практика\main\Самокаты.xlsx", engine='openpyxl',index_col=None)
df['Среднее количество'] = df[['Москва','Ногинск','Зеленоград','Щёлково', #Среднее
                                     'Химки','Подольск','Монино','Люберцы','Реутов',
                                     'Королёв','Сергиев-Пасад','Троицк','Серпухов',
                                     'Красногорск','Мытищи']].mean(axis=1)
df['Всего самокатов'] = df[['Москва','Ногинск','Зеленоград','Щёлково', #Сумма
                  'Химки','Подольск','Монино','Люберцы','Реутов',
                  'Королёв','Сергиев-Пасад','Троицк','Серпухов',
                  'Красногорск','Мытищи']].sum(axis=1)
df1 = df[(df['Москва'] >0)] # Сносим нули и используем его для дальнейших процедур
#print(df1)
#----------------------Создаём фреймы на сонове подсчётов за годы-------------------------------#
year_2020 = df1.loc[df1['Год'] == 2020] #Делаем выборку по 2020 году
year_2020_result = year_2020['Всего самокатов'] #Создаём df по итогам суммы
#print(year_2020_result)
year_2020_copy = year_2020['Всего самокатов'].copy() #Создаём копию DataFrame
#print(year_2020_copy)

year_2021 = df1.loc[df1['Год'] == 2021] #Делаем выборку по 2021 году
year_2021_result = year_2021['Всего самокатов'] #Создаём df по итогам суммы для библиотечек
#print(year_2021_result)
year_2021_copy = year_2021['Всего самокатов'].copy() #Создаём копию DataFrame для библиотечек
#print(year_2021_copy)

year_2022 = df1.loc[df1['Год'] == 2022] #Делаем выборку по 2022 году
year_2022_result = year_2022['Всего самокатов'] #Создаём df по итогам суммы
#print(year_2020_result)
year_2022_copy = year_2022['Всего самокатов'].copy() #Создаём копию DataFrame для библиотечек
#print(year_2022_copy)

year_2022_result.to_excel('всего за 2022.xlsx')
#year_2021_result.to_excel('всего за 2021.xlsx')
#year_2020_result.to_excel('всего за 2020.xlsx')


#-----------------------Создаём фреймы на сонове подсчётов за месяцы----------------------------#
april = df1.loc[df1['Месяц'] == "апрель"] #Месяц апрель
all_april = april['Среднее количество']
okrug_apr = df1['Среднее количество'].apply(np.floor)
#print(all_april)

may = df1.loc[df1['Месяц'] == "май"] #Месяц май
all_may = may['Среднее количество']
okrug_may = df1['Среднее количество'].apply(np.floor)
#print(all_may)

june = df1.loc[df1['Месяц'] == "июнь"] #Месяц июнь
df_june = pd.DataFrame(june)
#print(df_june)
all_june = june['Среднее количество']
okrug_june = df1['Среднее количество'].apply(np.floor)
print(all_june)

july = df1.loc[df1['Месяц'] == "июль"] #Месяц июль
all_july = july['Среднее количество']
okrug_july = df1['Среднее количество'].apply(np.floor)
#print(all_july)

august = df1.loc[df1['Месяц'] == "август"] #Месяц август
all_august = august['Среднее количество']
okrug_august = df1['Среднее количество'].apply(np.floor)
#print(all_august)

september = df1.loc[df1['Месяц'] == "сентябрь"] #Месяц сентябрь
all_september = september['Среднее количество']
okrug_september = df1['Среднее количество'].apply(np.floor)
#print(all_september)

october = df1.loc[df1['Месяц'] == "октябрь"] #Месяц октябрь
all_october = october['Среднее количество']
okrug_october = df1['Среднее количество'].apply(np.floor)
#print(all_october)

all_april.to_excel('апрель - среднее.xlsx')
all_may.to_excel('май - среднее.xlsx')
all_june.to_excel('июнь - среднее.xlsx')
all_july.to_excel('июль - среднее.xlsx')
all_august.to_excel('август - среднее.xlsx')
all_september.to_excel('сентябрь - среднее.xlsx')
all_october.to_excel('октябрь - среднее.xlsx')

#---------------------------------Слияние месячных фреймов:
frame_month = [all_april, all_may, all_june, all_july, all_august, all_september, all_october]
result_month = pd.concat(frame_month)
result_month1 = pd.DataFrame(result_month)
#print(frame_month)

#-------------------------------Временные интервалы:
months = pd.DataFrame(df1[["Месяц"]])
#print(months)
years = pd.DataFrame(df1[["Год"]])
print(years)

#months.to_excel('month.xlsx')
#years.to_excel('years.xlsx')

#----------------------Создаём фреймы на сонове аренды в регионах-------------------------------#
regions = df1[['Москва','Ногинск','Зеленоград','Щёлково',
               'Химки','Подольск','Монино','Люберцы','Реутов',
               'Королёв','Сергиев-Пасад','Троицк','Серпухов',
               'Красногорск','Мытищи']].copy()
regions.loc['Итого',:] = regions.sum(axis=0)
regions_total = regions.loc['Итого']
regions_total_forGraph = pd.DataFrame(regions_total)
#print(regions_total)
#print(regions_total_forGraph)

#-----------------------------------Выводим файлы в.xlsx---------------------------------------#
#-----------------Рабочие-----------------#
result_month1.to_excel("Месяцы - среднее.xlsx")
regions_total.to_excel("Регионы (Итого за 3 года).xlsx")

                                                #--------------Нерабочие--------------#
                                                #Не округляет переменную "okrug" в excel
                                                #okrug_apr.to_excel('апрель - среднее.xlsx')
                                                #okrug_may.to_excel('май - среднее.xlsx')
                                                #okrug_june.to_excel('июнь - среднее.xlsx')
                                                #okrug_july.to_excel('июль - среднее.xlsx')
                                                #okrug_august.to_excel('август - среднее.xlsx')
                                                #okrug_september.to_excel('сентябрь - среднее.xlsx')
                                                #okrug_october.to_excel('октябрь - среднее.xlsx')

#---------Основные---------#
df1.to_excel('result.xlsx')
#df.to_excel('С нулями.xlsx')

#------------------------------------------Графики--------------------------------------------#

regions_total_forGraph.plot(kind='bar', figsize=(10,6), ylabel='аренда')
plt.title("Уровень аренды самокатов в регионах")

result_month1.plot(kind='bar', figsize=(10,6), ylabel='уровень продаваемости в шт.')
plt.title("Гистограмма среднего значения")
plt.xlabel("в течение года")

df_june.plot(kind='bar', figsize=(10,6), ylabel='аренда')
plt.title("Уровень аренд в июне месяце")

#frame_circle = pd.DataFrame(years)
#frame_circle.groupby(df1.loc[df1['Год'] == "2020"], df1.loc[df1['Год'] == "2021"],
#                     df1.loc[df1['Год'] == "2022"]).sum().plot(kind='pie', y='years')

plt.show()