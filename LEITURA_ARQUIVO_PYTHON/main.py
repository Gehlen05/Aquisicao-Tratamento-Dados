import pandas as pd
import matplotlib.pyplot as plt
from os.path import basename
batimentos_dia = {}
# arquivo_entrada = ('heart_rate_short.csv')
arquivo_entrada = ('heart_rate_long.csv')
heart_rate = pd.read_csv(arquivo_entrada)
df = pd.DataFrame(heart_rate)
mean_df = df['heartRate'].mean()
desvio_df = df['heartRate'].std()
print(f'Media e: {mean_df}')
print(f'Desvio padrao e: {desvio_df}')
eixo_y = df['heartRate'].rolling(1200).mean()
# eixo_x = df['date'].apply(lambda x: str(x)[5:])
x = (range(len(eixo_y)))
plt.plot(x, eixo_y)
plt.title('BPM por dia')
plt.savefig(f'imagens/serie_temporal')
plt.cla()
date = df['date'].apply(lambda x: str(x))
eixo_x = df['time']
eixo_y = df['heartRate']
i = 0
for dias in date:
    batimentos_dia.setdefault(dias, []).append(eixo_y[i])
    i += 1
for dia, batimentos in batimentos_dia.items():
    df = pd.DataFrame(batimentos)
    batimentos_filtrados = df.rolling(60).mean()
    x = (range(len(batimentos_filtrados)))
    plt.plot(x, batimentos_filtrados)
    plt.title('BPM por dia')
    plt.xlabel('Dia')
    plt.ylabel('BPM')
    plt.savefig(f'imagens/{dia}')
    plt.cla()






# print(eixo_x)
# print(mean_df)
# print(desvio_df)
# plt.plot(eixo_x[:3600], eixo_y[:3600])
# plt.savefig(str(basename(arquivo_entrada)).split('.')[0])