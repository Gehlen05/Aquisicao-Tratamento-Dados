# https://github.com/Gehlen05/Aquisicao-Tratamento-Dados
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statistics


def _ler_arquivo(arquivo_entrada):
    heart_rate = pd.read_csv(arquivo_entrada)
    df = pd.DataFrame(heart_rate)
    df['date'] = pd.to_datetime(df['date'])
    df['time'] = pd.to_datetime(df['time'])
    return df

def _plotar_grafico(eixo_x, eixo_y, nome, titulo='Batimentos Dia'):
    plt.plot(eixo_x, eixo_y)
    plt.title(titulo)
    plt.xlabel('Tempo')
    plt.ylabel('BPM')
    plt.savefig(f'imagens/{nome}')
    plt.cla()

if __name__ == '__main__':
    df = _ler_arquivo('heart_rate_long.csv')
    df['day_year'] = df.date.dt.dayofyear
    print(df.head())
    ax = sns.barplot(x='day_year', y='heartRate', data=df, color="#4CB391")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
    plt.savefig(f'bpm_dia')
    plt.cla()
