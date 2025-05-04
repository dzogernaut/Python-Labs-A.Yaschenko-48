import matplotlib.pyplot as plt  # Для построения графиков

import seaborn as sns  # Для более красивой визуализации данных

from sklearn import datasets  # Для использования встроенных наборов данных

import pandas as pd  # Для работы с табличными данными


iris = datasets.load_iris()

iris_data = pd.DataFrame(data=iris.data, columns=iris.feature_names)
iris_data['species'] = iris.target

iris_data['species'] = iris_data['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})


plt.figure(figsize=(10, 6))
# Используем метод scatterplot из библиотеки Seaborn для построения графика
sns.scatterplot(data=iris_data,
                 x='sepal length (cm)',
                 y='sepal width (cm)',
                 hue='species',          # Различные виды цветков отмечаем разными цветами
                 style='species',
                 palette='deep')         # Количество и выбор цветов для графика

plt.title("Iris Sepal Size")
plt.xlabel("Длина чашелистиков (см)")
plt.ylabel("Ширина чашелистиков (см)")


plt.legend(title='Виды')
plt.show()

