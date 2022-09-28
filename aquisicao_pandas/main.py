import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def ler_arquivo(arquivo):
    heart_rate = pd.read_csv(arquivo_entrada)
    df = pd.DataFrame(heart_rate)
    df['date'] = pd.to_datetime(df['date'])
    df['time'] = pd.to_datetime(df['time'])
    return df


if __name__ == '__main__':
    arquivo_entrada = 'heart_rate_long.csv'

    # TENTAR AGRUPAR POR MES E DO MES POR SEMANA
    meses_ano = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                 'September', 'November', 'December')
    df = ler_arquivo(arquivo_entrada)

    # Agrupando atraves da data e criando coluna mes
    df['month'] = df.date.dt.month_name()
    df['week'] = df.date.dt.isocalendar().week
    df['day'] = df.date.dt.day_name()
    df['day_week'] = df.date.dt.isocalendar().day
    df['day_month'] = df.date.dt.daysinmonth
    df['day_year'] = df.date.dt.dayofyear

    for mes in meses_ano:
        df_novo = df[df['month'] == mes]
        if not df_novo.empty:
            # Plota a media das semanas do mes
            ax = sns.barplot(x='week', y='heartRate', data=df_novo, color="#4CB391")
            ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
            plt.savefig(f'bpm_semana_mes_{mes}')
            plt.cla()

    for semana in range(16, 33):
        df_novo = df[df['week'] == semana]
        if not df_novo.empty:
            # Plota os dias de cada semana
            ax = sns.barplot(x='day', y='heartRate', data=df_novo, color="#4CB391")
            ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
            plt.savefig(f'bpm_semana_{semana}')
            plt.cla()

    df = ler_arquivo(arquivo_entrada)
    # agrupando por mes e fazendo a media e maxima
    mes_medio = df.groupby(by=df.date.dt.month_name()).mean(['heartRate']).reset_index()
    mes_maximo = df.groupby(by=df.date.dt.month_name()).max(['heartRate']).reset_index()

    fig, axes = plt.subplots(1, 2, figsize=(20, 10), sharey=True)
    fig.suptitle('Media e máxima ao longo dos meses')

    ax = sns.barplot(ax=axes[0], x='date', y='heartRate', data=mes_medio, color="#4CB391")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
    axes[0].set_title('Media mes')

    ax = sns.barplot(ax=axes[1], x='date', y='heartRate', data=mes_maximo, color="#4CB391")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
    axes[1].set_title('Máximo mes')

    plt.savefig(f'bpm_mes_media_maxima')
    plt.cla()

    semana_medio = df.groupby(by=df.date.dt.isocalendar().week).mean(['heartRate']).reset_index()
    semana_maximo = df.groupby(by=df.date.dt.isocalendar().week).max(['heartRate']).reset_index()

    fig, axes = plt.subplots(1, 2, figsize=(20, 10), sharey=True)
    fig.suptitle('Media e máxima ao longo das semanas')

    ax = sns.barplot(ax=axes[0], x='week', y='heartRate', data=semana_medio, color="#4CB391")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
    axes[0].set_title('Semana media mes')

    ax = sns.barplot(ax=axes[1], x='week', y='heartRate', data=semana_maximo, color="#4CB391")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
    axes[1].set_title('Semana maxim mes')

    plt.savefig(f'bpm_semana_media_maxima')
    plt.cla()

    dia_medio = df.groupby(by=df.date.dt.dayofyear).mean(['heartRate']).reset_index()
    dia_maximo = df.groupby(by=df.date.dt.dayofyear).max(['heartRate']).reset_index()

    ax = sns.barplot(ax=axes[0], x='date', y='heartRate', data=dia_medio, color="#4CB391")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
    axes[0].set_title('Media mes')

    ax = sns.barplot(ax=axes[1], x='date', y='heartRate', data=dia_maximo, color="#4CB391")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
    axes[1].set_title('Máximo mes')

    plt.savefig(f'bpm_dia_media_maxima')
    plt.cla()
