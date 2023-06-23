import matplotlib
import matplotlib.pyplot as plt
import io
import base64
import pandas as pd
import seaborn as sns
from statsmodels.tsa.arima.model import ARIMA
from pmdarima.arima import auto_arima
matplotlib.use('Agg')


file_path = 'cleaned_data.xlsx'
table5_data = pd.read_excel(file_path, sheet_name='Table 5')


def perform_trend_analysis():
    table5_data = pd.read_excel(file_path, sheet_name='Table 5')
    table5_data['date'] = pd.to_datetime(table5_data[['year', 'month']].assign(day=1))  
    table5_data = table5_data.sort_values('date')

    plt.figure(figsize=(10, 6))
    plt.plot(table5_data['date'], table5_data['average_wages'], label='Average Wages')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.title('Trend Analysis: Average Wages')
    plt.legend()
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plot_data = base64.b64encode(buffer.read()).decode('utf-8')
    plt.close()

    return plot_data


def perform_seasonal_analysis():
    aggregated_data = table5_data.groupby('month')['average_wages'].mean().reset_index()

    plt.figure(figsize=(10, 6))
    sns.lineplot(x=aggregated_data['month'], y=aggregated_data['average_wages'], errorbar=None)
    plt.xlabel('Month')
    plt.ylabel('Average Wages')
    plt.title('Seasonal Analysis: Average Wages')
    plt.legend(['Average Wages'])

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plot_data = base64.b64encode(buffer.read()).decode('utf-8')
    plt.close()

    return plot_data


def perform_summary_statistics():
    table5_stats = table5_data['average_wages'].describe().to_frame().reset_index()

    return table5_stats


def perform_predictive_analysis():
    model = auto_arima(table5_data['average_wages'], start_p=0, start_q=0, max_p=3, max_q=3, d=None, seasonal=False, trace=True)
    best_p, best_d, best_q = model.order
    model2 = ARIMA(table5_data['average_wages'], order=(best_p, best_d, best_q))
    model_fit = model2.fit()
    predictions = model_fit.predict(start=len(table5_data), end=len(table5_data)+18, typ='levels')
    predicted_wages = predictions.tolist()

    return predicted_wages
