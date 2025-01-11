# pip install flask pandas alpha_vantage matplotlib plotly
# Najnowsza wersja Pythona 3.13

from flask import Flask, render_template, request
from alpha_vantage.timeseries import TimeSeries
import pandas as pd
import os
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt

app = Flask(__name__)

API_key = 'YCCRH0E6VQMXU42V'  # przypisanie kluczu API

@app.route("/", methods=["GET", "POST"])
def index():
    stock_data = None
    descriptive_stats = None
    chart_paths = {}
    if request.method == "POST":
        symbol = request.form["symbol"]
        ts = TimeSeries(key=API_key, output_format='json')
        data, meta_data = ts.get_daily(symbol=symbol, outputsize='compact')

        # Przedstawienie danych w formie tabeli
        df = pd.DataFrame.from_dict(data, orient='index')
        df.columns = ['Open', 'High', 'Low', 'Close', 'Volume']
        df.index = pd.to_datetime(df.index)  # uporządkowanie danych względem daty
        df = df.sort_index()

        # Konwersja kolumn na typy numeryczne
        df['Open'] = pd.to_numeric(df['Open'])
        df['High'] = pd.to_numeric(df['High'])
        df['Low'] = pd.to_numeric(df['Low'])
        df['Close'] = pd.to_numeric(df['Close'])
        df['Volume'] = pd.to_numeric(df['Volume'])

        # Obliczanie statystyk opisowych
        mean_close = df['Close'].mean()
        median_close = df['Close'].median()
        max_close = df['Close'].max()
        min_close = df['Close'].min()
        std_close = df['Close'].std()
        var_close = df['Close'].var()

        # Tworzenie stringu z wynikami
        descriptive_stats = {
            "mean_close": mean_close,
            "median_close": median_close,
            "max_close": max_close,
            "min_close": min_close,
            "std_close": std_close,
            "var_close": var_close
        }

        stock_data = df.to_html(classes="table table-striped")

        # Generowanie stopy zwrotu
        df['Return'] = df['Close'].pct_change()

        # Tworzenie wykresów za pomocą Matplotlib
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 6))

        # Wykres cen zamknięcia
        ax1.plot(df.index, df['Close'], label='Close Price', color='lightblue')
        ax1.set_xlabel('Data')
        ax1.set_ylabel('Cena zamknięcia')
        ax1.set_title(f'Wykres cen zamknięcia dla {symbol}')
        ax1.grid(True, linestyle='--', alpha=0.6)
        ax1.legend()
        ax1.tick_params(axis='x', rotation=45)

        # Wykres wolumenu
        volume = df['Volume'].astype(float)
        ax2.bar(df.index, volume, color='purple', label='Volume')
        ax2.set_xlabel('Data')
        ax2.set_ylabel('Wolumen (Volume)')
        ax2.set_title(f'Wolumen dla {symbol}')
        ax2.grid(True, linestyle='--', alpha=0.6)
        ax2.tick_params(axis='x', rotation=45)
        ax2.legend()

        plt.tight_layout()
        plt.savefig('static/close_volume_plots.png')
        plt.close()
        chart_paths['close_volume'] = 'static/close_volume_plots.png'

        # Generowanie pozostałych interaktywnych wykresów
        fig_hist = px.histogram(df, x='Close', nbins=30, marginal="violin",
                                title=f'Histogram dla wartości Zamknięcia ({symbol})',
                                color_discrete_sequence=['lightgreen'])
        fig_hist.update_layout(bargap=0.1)
        hist_path = f'static/{symbol}_hist.html'
        fig_hist.write_html(hist_path)
        chart_paths['hist'] = hist_path

        fig_box = px.box(df, y='Close', title=f'Boxplot dla wartości Zamknięcia ({symbol})',
                         color_discrete_sequence=['purple'])
        box_path = f'static/{symbol}_box.html'
        fig_box.write_html(box_path)
        chart_paths['box'] = box_path

        melted_df = pd.melt(df[['Close']], var_name='Price Type', value_name='Price')
        fig_violin = px.violin(melted_df, x='Price Type', y='Price', box=True, points="all",
                               title=f'Violin plot dla zmiennej Zamknięcia ({symbol})',
                               color='Price Type')
        violin_path = f'static/{symbol}_violin.html'
        fig_violin.write_html(violin_path)
        chart_paths['violin'] = violin_path

        # Interaktywny wykres dla stopy zwrotu
        fig_return = go.Figure()
        fig_return.add_trace(go.Scatter(x=df.index, y=df['Return'], mode='lines', name='Return',
                              line=dict(color='blue')))
        fig_return.update_layout(
            title=f'Stopy Zwrotu dla wartości Zamknięcia ({symbol})',
            xaxis_title='Data',
            yaxis_title='Stopa Zwrotu',
            xaxis_rangeslider_visible=True
        )
        return_path = f'static/{symbol}_return.html'
        fig_return.write_html(return_path)
        chart_paths['return'] = return_path

    return render_template("index.html", stock_data=stock_data, descriptive_stats=descriptive_stats, chart_paths=chart_paths)

if __name__ == "__main__":
    if not os.path.exists('static'):
        os.makedirs('static')
    app.run(debug=True)
