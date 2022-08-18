import click
import pandas as pd
from sklearn.model_selection import train_test_split

@click.command()
@click.argument("input_raw_train_path", type=click.Path(exists=True))
@click.argument("output_split_train_path", type=click.Path())
@click.argument("output_split_test_path", type=click.Path())
@click.option("train_size", default=0.1, type=click.INT)
def train_test_group_split_csv(
    input_raw_train_path: str,
    output_split_train_path: str,
    output_split_test_path: str,
    train_size = 0.1,
) -> None:
    """Разбиваем исходный train датасет на train/test.
    Args:
        input_raw_train_path (str): Путь до исходного датасета .csv (обычно train.csv)
        output_split_train_path (str): Путь до выходного split_train.csv
        output_split_test_path (str): Путь до выходного split_test.csv
        n_splits (int, optional): Количество частей, на которые будет разбит train датасет,
        при этом, одна из частей уйдет на split_test, все остальные на split_train,
        например: 3 = 1/2 (или 33%/88%), 4 = 1/3 (или 25%/75) и т.д.. Defaults to 3:int.
    """
    raw_train = pd.read_excel(input_raw_train_path)
    raw_train["hour"] = raw_train['date'].apply(lambda x: x.hour)
    raw_train["weekday"] = raw_train['date'].apply(lambda x: x.weekday())

    split_train, split_test = train_test_split(raw_train, train_size=train_size, shuffle=False)

    split_train.to_excel(output_split_train_path, index=False)
    split_test.to_excel(output_split_test_path, index=False)


if __name__ == "__main__":
    train_test_group_split_csv()  # pylint: disable=E1120
