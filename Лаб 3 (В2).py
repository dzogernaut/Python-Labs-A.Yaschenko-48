# Импортируем модуль pyplot из библиотеки matplotlib, который используется для создания графиков и визуализаций
import matplotlib.pyplot as plt
# Импортируем модуль nile из библиотеки statsmodels.datasets, который содержит набор данных о годовом расходе воды в реке Нил
from statsmodels.datasets import nile


data = nile.load_pandas().data

# Устанавливаем столбец 'year' (год) в качестве индекса DataFrame.
data.set_index('year', inplace=True)


plt.figure(figsize=(10, 6))

plt.plot(data['volume'], label='Годовой расход воды в реке Нил')

plt.title('Годовой расход воды в реке Нил (1871-1970)')
plt.xlabel('Год')
plt.ylabel('Годовой расход воды (кубические гектометры)')
plt.legend()

plt.grid(True)

plt.show()
