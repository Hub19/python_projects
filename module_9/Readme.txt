Car Price prediction

Задача предсказать стоимость автомобиля по имеющейся информации о характеристиках, текстах объявлений и картинках.

	•	Построили "наивную"/baseline модель, предсказывающую цену по модели и году выпуска (с ней будем сравнивать другие модели)
	•	Обработали и отнормировали признаки
	•	Сделали первую модель на основе градиентного бустинга с помощью CatBoost
	•	Сделали вторую модель на основе нейронных сетей и сравнили результаты
	•	Сделали multi-input нейронную сеть для анализа табличных данных и текста одновременно
	•	Добавили в multi-input сеть обработку изображений
	•	Осуществили ансамблирование градиентного бустинга и нейронной сети (усреднение их предсказаний)
