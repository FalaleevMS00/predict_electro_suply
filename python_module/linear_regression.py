from sklearn.linear_model import LinearRegression
from features_for_model import feat_eng, feat_eng_1,feat_eng_2
from datetime import timedelta
import numpy as np



# новый код

temp = train.copy()
temp_4_pred = temp.copy()
front_predict = len(test)
for i in range(front_predict):
    # добавили фичи
    temp_4_fit = temp.copy()
    temp_4_fit = feat_eng(feat_eng_1(feat_eng_2(temp_4_fit)))
    temp_4_fit = temp_4_fit.dropna()
    temp_4_fit = temp_4_fit.reset_index(drop=True)
    # подготовили иксы и игрики для модели
    X_train_4_fit = temp_4_fit.drop(['Потребитель', 'date'], axis=1)
    y_train_4_fit = temp_4_fit['Потребитель']
    # протренировали модель
    lr = LinearRegression()
    lr.fit(X_train_4_fit, y_train_4_fit)
    # создаём следуюущее значение которое надо предсказать
    # создадим новую строку, в основном, надо чтобы была добавлена дата на час вперед, остальные знаения будут в нуле

    temp_4_pred.loc[len(temp_4_pred), 'date'] = temp_4_pred['date'].iloc[-1] + timedelta(hours=1)
    temp_4_pred.loc[len(temp_4_pred), 'Потребитель'] = np.nan
    temp_4_pred["hour"] = temp_4_pred['date'].apply(lambda x: x.hour)
    temp_4_pred["weekday"] = temp_4_pred['date'].apply(lambda x: x.weekday())
    temp_4_pred = feat_eng(feat_eng_1(feat_eng_2(temp_4_pred)))
    temp_4_pred = temp_4_pred[:-1]
    # на данном этапе имеем датафрейм с одной добавленной строкой и одни пустым значением в искомом столбце
    # выделим строку для предсказания
    value_4_pred = temp_4_pred.tail(1)
    X_train_4_pred = value_4_pred.drop(['Потребитель', 'date'], axis=1)
    X_train_4_pred = X_train_4_pred.fillna(0)
    # предсказываем значение
    predict_consumer = lr.predict(X_train_4_pred)
    temp_4_pred.loc[len(temp_4_pred) - 1, 'Потребитель'] = float(predict_consumer)
    temp = temp_4_pred.copy()
final_proverka = temp_4_pred.copy()
final = temp_4_pred.copy().loc[len(final_proverka) - front_predict:][['date', 'Потребитель']]
