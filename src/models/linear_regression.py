from sklearn.linear_model import LinearRegression
from features_for_model import feat_eng, feat_eng_1, feat_eng_2
from datetime import timedelta
import numpy as np
import pandas as pd
import click

@click.command()
@click.argument("input_pair_features_train_dataset_path", type=click.Path(exists=True))
@click.argument("input_pair_features_test_dataset_path", type=click.Path(exists=True))
@click.argument("output_model_path", type=click.Path())
@click.argument("output_submission_path", type=click.Path())
@click.argument("output_metrics_path", type=click.Path())
def train_model(
        input_pair_features_train_dataset_path: str,
        input_pair_features_test_dataset_path: str,
        output_predict_dataset_path: str
):
    train = pd.read_excel(input_pair_features_train_dataset_path)
    test = pd.read_excel(input_pair_features_test_dataset_path)
    temp = train.copy()
    temp_4_pred = temp.copy()
    front_predict = len(test)
    for i in range(front_predict):
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

        # если я правильно всё понимаю то освободим память
        del temp_4_fit, X_train_4_fit, y_train_4_fit

        # создаём следуюущее значение которое надо предсказать
        # создадим новую строку, в основном, надо чтобы была добавлена дата на час вперед, остальные значения будут в нуле
        temp_4_pred.loc[len(temp_4_pred), 'date'] = temp_4_pred['date'].iloc[-1] + timedelta(hours=1)
        temp_4_pred.loc[len(temp_4_pred), 'Потребитель'] = np.nan
        # добавляем фичи
        temp_4_pred["hour"] = temp_4_pred['date'].apply(lambda x: x.hour)
        temp_4_pred["weekday"] = temp_4_pred['date'].apply(lambda x: x.weekday())
        temp_4_pred = feat_eng(feat_eng_1(feat_eng_2(temp_4_pred)))
        temp_4_pred = temp_4_pred[:-1] # + потерял в счёте который костыль
        # на данном этапе имеем датафрейм с одной добавленной строкой и одним пустым значением в искомом столбце
        # выделим строку для предсказания
        value_4_pred = temp_4_pred.tail(1)
        X_train_4_pred = value_4_pred.drop(['Потребитель', 'date'], axis=1)
        # X_train_4_pred = X_train_4_pred.fillna(0) проверить нужна ли строка
        # предсказываем значение
        predict_consumer = lr.predict(X_train_4_pred)
        # добавляем в датафрейм предсказанное значение
        temp_4_pred.loc[len(temp_4_pred) - 1, 'Потребитель'] = float(predict_consumer)
        # переопределяем исходный датасет с добавлением новой строки и идем дальше в цикл
        temp = temp_4_pred.copy()
    final_test = temp_4_pred.copy()
    final = temp_4_pred.copy().loc[len(final_test) - front_predict:][['date', 'Потребитель']]
    final.to_excel(output_predict_dataset_path, index=False)

if __name__ == "__main__":
    train_model()

#по итогу создан датасет с предсказанными значениями, однако этот код расчитан на то, что он будет сравниваться
# с отложенными данными, надо будет создать функция, которая не будет привязана к тестовым данным