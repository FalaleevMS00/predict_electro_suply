import pandas as pd
import click
from datetime import timedelta

@click.command()
@click.argument("input_path", type=click.Path(exists=True))
@click.argument("output_path", type=click.Path())
def clean_data(input_path: str, output_path: str):
    """
    Create new format of date in input dataframe
    :param input_path: path with input data
    :param output_path: path to save file
    """
    data = pd.read_csv(input_path)
# обработка 24 часа
    data.loc[(data['часы'] == 24), 'Дата'] = data.loc[(data['часы'] == 24), 'Дата'] + timedelta(days=1)
    data.loc[(data['часы'] == 24), 'часы'] = 0
# преобразуем значения колонок 'Дата', 'часы' в строку
    data['Дата'] = data['Дата'].astype(str)
    data['часы'] = data['часы'].astype(str)
# создадим новую колонку
    data['date'] = data['Дата'] + "-" + data['часы']
    data['date'] = pd.to_datetime(data['date'], format='%Y-%m-%d-%H')
# отберем только нужные колонки
    data_clean = data[['date', 'Потребитель']]
# сохраним полученное
    data_clean.to_excel(output_path, index=False)

if __name__ == "__main__":
    clean_data()
