# https://github.com/Gehlen05/Aquisicao-Tratamento-Dados
import pandas as pd
import matplotlib.pyplot as plt
import statistics


def _ler_arquivo(arquivo_entrada):
    heart_rate = pd.read_csv(arquivo_entrada)
    data_frame = pd.DataFrame(heart_rate)
    return data_frame


def _separar_dia(data_frame):
    batimentos_diarios = {}
    datas = data_frame['date']
    i = 0
    batimentos = data_frame['heartRate']
    for data in datas:
        batimentos_diarios.setdefault(data, []).append(batimentos[i])
        i += 1
    return batimentos_diarios


def _plotar_grafico(eixo_x, eixo_y, nome, titulo='Batimentos Dia'):
    plt.plot(eixo_x, eixo_y)
    plt.title(titulo)
    plt.xlabel('Tempo')
    plt.ylabel('BPM')
    plt.savefig(f'imagens/{nome}')
    plt.cla()


def _todos_dias_media_movel(data_frame):
    mean_data_frame = data_frame['heartRate'].mean()
    desvio_data_frame = data_frame['heartRate'].std()
    print(f'Media e: {mean_data_frame}')
    print(f'Desvio padrao e: {desvio_data_frame}')
    eixo_y = data_frame['heartRate'].rolling(86400).mean()
    x = (range(len(eixo_y)))
    _plotar_grafico(x, eixo_y, 'serie_temporal_media_movel_diaria')


def _media_total_(data_frame):
    batimentos_diarios = _separar_dia(data_frame)
    batimento_media_diaria = []
    for data, batimento in batimentos_diarios.items():
        batimento_media_diaria.append(statistics.mean(batimento))
    _plotar_grafico(batimentos_diarios.keys(), batimento_media_diaria, 'temporal_media_statistics_dia')


def _media_diaria_minuto(data_frame):
    batimentos_diarios = _separar_dia(data_frame, 'time')
    for dia, batimentos in batimentos_diarios.items():
        data_frame = pd.DataFrame(batimentos)
        batimentos_filtrados = data_frame.rolling(60).mean()
        x = (range(len(batimentos_filtrados)))
        _plotar_grafico(x, batimentos_filtrados, dia)

def _media_diaria_hora(data_frame):
    batimentos_diarios = {}
    datas = data_frame['date']
    hora = data_frame['time'].astype(str)
    batimentos = data_frame['heartRate']
    i = 0
    for data in datas:
        batimentos_diarios.setdefault(data, {'hora': [], 'batimentos': []})
        batimentos_diarios[data]['batimentos'].append(batimentos[i])
        batimentos_diarios[data]['hora'].append(hora[i][:2])
        i += 1
    for dia, dados in batimentos_diarios.items():
        data_frame_batimentos = dados['batimentos']
        data_frame_hora = dados['hora']
        for hora in data_frame_hora:
            horarios = {}
            i = 0
            for hora in data_frame_hora:
                # print(type(hora))
                # print(hora)
                horarios.setdefault(hora, []).append(data_frame_batimentos[i])
                i += 1
            batimentos_hora = []
            for hora, batimentos in horarios.items():
                batimentos_hora.append(statistics.mean(batimentos))
            _plotar_grafico(horarios.keys(), batimentos_hora, f'{dia}_hora')

        # hora = list(range(0, 24, 1))
        # batimentos_filtrados = data_frame_batimentos.rolling(3600).mean()
        # print(len(data_frame_batimentos))
        # print(len(batimentos_filtrados))
        # # x = (range(len(batimentos_filtrados)))


if __name__ == '__main__':
    data_frame = _ler_arquivo('heart_rate_long.csv')
    # _todos_dias_media_movel(data_frame)
    # _media_total_(data_frame)
    # _media_diaria_minuto(data_frame)
    _media_diaria_hora(data_frame)
