from sklearn.metrics import mean_absolute_error, mean_squared_error
import pandas as pd
import click

@click.command()
@click.argument("input_dataset_test_path", type=click.Path(exists=True))
@click.argument("input_dataset_predict_path", type=click.Path(exists=True))
@click.argument("output_metric", type=click.Path())

def metric(input_dataset_test_path: str,
        input_dataset_predict_path: str,
        output_metric: str
):
    test = pd.read_excel(input_dataset_test_path)
    pred = pd.read_excel(input_dataset_predict_path)
    test_supply = test['Потребитель']
    pred_supply = pred['Потребитель']
    score = pd.DataFrame(data = {'Модель' : 'Linear Regression',
                                 'RMSE' : [round(mean_squared_error(test_supply, pred_supply, squared=False), 1)],
                                 'MAE' : [round(mean_absolute_error(test_supply, pred_supply), 1)] ,
                                 'Промежуток прогнозирования' : 'Неделя', 'Дискретность' : 'Часы',})
    score.to_excel(output_metric, index=False)

if __name__ == "__main__":
    metric()