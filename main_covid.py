import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# импморт библиотек

#####################
# сформировали данные
#####################

dataFrame = pd.read_csv(r"C:\Users\Alexey\Desktop\корона\covid19.csv")
# открытие файла
dataFrame.shape 
# показ даты перед чисткой

#######################
#######################
#######################

#######################
# очистка
#######################

dataFrame = dataFrame.dropna() # показ даты после чистки, убрать NaN параметры

#######################
#######################
#######################


Russia_DB = dataFrame[dataFrame['country'] == 'Russia']
Ukraine_DB = dataFrame[dataFrame['country'] == 'Ukraine']
Afghanistan_DB = dataFrame[dataFrame['country'] == 'Afghanistan']
Kazakhstan_DB = dataFrame[dataFrame['country'] == 'Kazakhstan']
Turkey_DB = dataFrame[dataFrame['country'] == 'Turkey']
print("shape of Russia_DB ", Russia_DB.shape)
print("shape of Ukraine_DB ", Ukraine_DB.shape)
print("shape of Afghanistan_DB ", Afghanistan_DB.shape)
print("shape of Kazakhstan_DB ", Kazakhstan_DB.shape)
print("shape of Turkey_DB ", Turkey_DB.shape)
# показ 5 выбранных стран
combined_df = pd.concat([Russia_DB, Ukraine_DB, Afghanistan_DB, Kazakhstan_DB, Turkey_DB])
# показ скомбинированных скран из даты
print("Shape of combined_df: ", combined_df.shape)


#######################
# тоже очистка (удаление столбцов)
#######################

from tabulate import tabulate
# вывод 10 строк/столбцов из даты
combined_df = combined_df.iloc[:, 1:]
# вывод 1 колонки из показа
combined_df = combined_df.drop('continent', axis=1)
# вывод континетов из даты
combined_df = combined_df.drop('day', axis=1)
# вывод колонки дня ибо есть колонка времени
print(tabulate(combined_df.head(10), headers='keys', tablefmt='psql'))
# мы выводим 10 строк

statistics = combined_df.describe()
# выдаем описание для combined_df
table = tabulate(statistics, headers='keys', tablefmt='fancy_grid')
# строчка сделана для красивого вида
print("Statistical Characteristics:")
print(table)
# 

#######################
#######################
#######################

#######################
# вывод данных в txt file
#######################
statistics.to_csv("statistical_characteristics.txt", sep='\t')

#######################
#######################
#######################

#######################
#######################
#######################
#######################

# гипотеза 1 Testing Rate и Cases Recovery
# извлечение нужных столбиков из даты
tests_total = Russia_DB['tests_total']
cases_recovered = Russia_DB['cases_recovered']

# создание диаграаммы вида scatter
plt.gca().get_yaxis().set_major_formatter(plt.FuncFormatter(lambda y, _: '{:,.0f}'.format(y)))
plt.scatter(tests_total, cases_recovered, marker='o', s=1, c='blue', alpha=0.5)
plt.title('Testing Rate vs. Cases Recovery')
plt.xlabel('Number of Tests Conducted')
plt.ylabel('Number of Cases Recovered')
plt.show()

def predict_cases_recovered(tests_total, cases_recovered, new_tests_total):
    # Преобразование данных в двумерные массивы
    tests_total = np.array(tests_total)  # Преобразование tests_total в массив numpy
    cases_recovered = np.array(cases_recovered)  # Преобразование cases_recovered в массив numpy
    # Вычисление среднего и ковариации данных
    mean_tests = np.mean(tests_total)  # Вычисление среднего значения tests_total
    mean_cases = np.mean(cases_recovered)  # Вычисление среднего значения cases_recovered
    covariance = np.cov(tests_total.flatten(), cases_recovered)[0][1]  # Вычисление ковариации между tests_total и cases_recovered
    # Вычисление коэффициента наклона и пересечения линии регрессии
    slope = covariance / np.var(tests_total)  # Вычисление коэффициента наклона (наклон регрессионной прямой)
    intercept = mean_cases - (slope * mean_tests)  # Вычисление пересечения (смещение регрессионной прямой)
    # Предсказание числа выздоровевших для нового количества тестов
    # f(xi) = C + Slope*xi
    predicted_cases_recovered = intercept + (slope * new_tests_total)  # Предсказание числа выздоровевших случаев для нового количества тестов

    # Построение графика данных и линии регрессии
    plt.scatter(tests_total, cases_recovered, marker='o', s=1, c='blue', alpha=0.5)  # Диаграмма рассеяния для tests_total и cases_recovered
    plt.plot(tests_total, intercept + slope * tests_total, color='red', label='Линейная регрессия')  # Линия регрессии (линейная аппроксимация данных)
    plt.xlabel('Количество тестов')  # Подпись оси x
    plt.ylabel('Выздоровевшие случаи')  # Подпись оси y
    plt.title('Линейная регрессия: Количество тестов vs. Выздоровевшие случаи')  # Заголовок графика
    plt.legend()  # Отображение легенды
    plt.show()  # Отображение графика

    return round(predicted_cases_recovered)  # Возврат предсказанного числа выздоровевших случаев (округленного)

# вызов функции для предсказания числа
predicted_cases = predict_cases_recovered(tests_total, cases_recovered, 273300000)
print("Predicted Cases Recovered:", predicted_cases)

#######################
#######################
#######################

# гипотеза 2: Population и Total Deaths
# извлечение нужных столбиков из даты
population = Russia_DB['population']
deaths_total = Russia_DB['deaths_total']
# создание диаграаммы вида scatter
plt.scatter(population, deaths_total, marker='o', s=1, c='red', alpha=0.5)
plt.title('Population vs. Total Deaths')
plt.xlabel('Population')
plt.ylabel('Total Deaths')
# Format x-axis tick labels as whole numbers
plt.xticks(rotation=45)
plt.gca().get_xaxis().set_major_formatter(plt.FuncFormatter(lambda x, _: '{:,.0f}'.format(x)))
plt.show()

def predict_total_death(population, deaths_total, new_population_total):
    # Преобразование данных в двумерные массивы
    population = np.array(population) # Преобразование population в массив numpy
    deaths_total = np.array(deaths_total) # Преобразование deaths_total в массив numpy
    # Вычисление среднего и ковариации данных
    mean_population = np.mean(population) # Вычисление среднего значения population
    mean_deaths = np.mean(deaths_total) # Вычисление среднего значения deaths_total
    covariance = np.cov(population.flatten(), deaths_total)[0][1] # Вычисление ковариации между population и deaths_total
   # Вычисление коэффициента наклона и пересечения линии регрессии
    slope = covariance / np.var(population) # Вычисление коэффициента наклона (наклон регрессионной прямой)
    intercept = mean_deaths - (slope * mean_population) # Вычисление пересечения (смещение регрессионной прямой)
    # Предсказание числа умерших к популяции
    # f(xi) = C + Slope*xi
    predicted_total_deaths = intercept + (slope * new_population_total) #предсказание смертности к популяции

 
    # Построение графика данных и линии регрессии
    plt.scatter(population, deaths_total, marker='o', s=1, c='red', alpha=0.5) # Диаграмма рассеяния для deaths_total_total и population
    plt.plot(population, intercept + slope * population, color='blue', label='Linear Regression') # Линия регрессии (линейная аппроксимация данных)
    plt.xlabel('Population') # Подпись оси x
    plt.ylabel('Total Deaths') # Подпись оси y
    plt.title('Линейная регрессия: Population vs. Total Deaths')  # Заголовок графика
    plt.legend() # Отображение легенды
    plt.xticks(rotation=45)  # поворот на 45 градусов для лучшей видимости
    plt.gca().get_xaxis().set_major_formatter(plt.FuncFormatter(lambda x, _: '{:,.0f}'.format(x)))
    plt.show()

    return round(predicted_total_deaths)

# пример использования
predicted_total_death = predict_total_death(population, deaths_total, 146000100)
# вывод результатов
print("Predicted Total death:", predicted_total_death)

#######################
#######################
#######################

# Гипотеза 3: Время и общее количество случаев
import matplotlib.dates as mdates
# Преобразование столбец времени в объекты datetime
time = pd.to_datetime(Russia_DB['time'])
# извлечение колонн в дату 
cases_total = Russia_DB['cases_total']
# создание диаграаммы вида scatter
plt.scatter(time, cases_total, marker='o', s=1, c='green', alpha=0.5)
plt.gca().xaxis.set_major_locator(mdates.MonthLocator()) # вывод в месяца и года
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))  # вывод в месяца и года
plt.gca().get_yaxis().set_major_formatter(plt.FuncFormatter(lambda y, _: '{:,.0f}'.format(y)))
plt.title('Time vs. Total Cases')
plt.xlabel('Time')
plt.ylabel('Total Cases')
plt.xticks(rotation=45)  # Rotate x-axis labels for better visibility
plt.show()

def predict_cases_total(time, cases_total, new_time):
    # перевод даты в номерной формат
    time_numeric = pd.to_datetime(time).astype(np.int64) // 10**9
    time_numeric = time_numeric.values  # конвертация в NumPy array
    new_time_numeric = pd.to_datetime(new_time).timestamp()

    # остальная часть кода такая же как и в предыдущих
    # вычисление среднего значение и ковариацию данных
    mean_time = np.mean(time_numeric)
    mean_cases = np.mean(cases_total)
    covariance = np.cov(time_numeric.flatten(), cases_total)[0][1]

    # вычисление наклона и пересечение линейной регрессии
    slope = covariance / np.var(time_numeric)
    intercept = mean_cases - (slope * mean_time)

    # f(xi) = C + Slope*xi
    predicted_cases = intercept + (slope * new_time_numeric) #предсказание смертности к популяции

     # Построение графика данных и линии регрессии
    plt.scatter(time_numeric, cases_total, marker='o', s=1, c='green', alpha=0.5)
    plt.plot(time_numeric, intercept + slope * time_numeric, color='red', label='Linear Regression')
    plt.xlabel('Time') # подпись х
    plt.ylabel('Total Cases') #подпись y
    plt.title('Линейная регрессия: Time vs. Total Cases') # название заголовка
    plt.legend()
    plt.show()

    return round(predicted_cases)

new_time = '2021-01-01'
predicted_cases = predict_cases_total(Russia_DB['time'], Russia_DB['cases_total'], new_time)
# вывод результатов
print("Predicted cases:", predicted_cases)