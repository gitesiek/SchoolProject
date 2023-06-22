import matplotlib
import matplotlib.pyplot as plt
import io
import base64
import pandas as pd
matplotlib.use('Agg')


file_path = '../cleaned_data.xlsx'
table5_data = pd.read_excel(file_path, sheet_name='Table 5')


def perform_trend_analysis():
    plt.figure(figsize=(16, 9))
    plt.plot(table5_data['year'], table5_data['average_wages'], label='Average Wages')
    plt.xlabel('Year')
    plt.ylabel('Value')
    plt.title('Trend Analysis: Average Employment and Average Wages')
    plt.legend()
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plot_data = base64.b64encode(buffer.read()).decode('utf-8')
    plt.close()

    return plot_data
