# Bibliotecas
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Importando a base de dados
Base_dados = pd.read_excel('Dados_Bitcoin.xlsx')

# Visualizando os dados
print(Base_dados.head(10))
print(Base_dados.info())

# Definindo a coluna 'Date' como índice
Base_dados.set_index('Date', inplace=True)

# Gráfico simples com Plotly Express
fig = px.line(Base_dados, y='Close', title='Fechamento do Bitcoin')
fig.show()

# Calculando médias móveis
Media_movel = Base_dados['Close'].rolling(5).mean()
Media_Tendencia = Base_dados['Close'].rolling(30).mean()

# Criando o gráfico com médias móveis
Figure = go.Figure()

# Linha de fechamento
Figure.add_trace(
    go.Scatter(
        x=Base_dados.index,
        y=Base_dados['Close'],
        mode='lines',
        name='Fechamento',
        line=dict(color='#ff7f0e'),
        opacity=0.7
    )
)

# Média Móvel Curta
Figure.add_trace(
    go.Scatter(
        x=Base_dados.index,
        y=Media_movel,
        mode='lines',
        name='Média Móvel 5 dias',
        line=dict(color='#a435c9', dash='dot'),
        opacity=0.7
    )
)

# Tendência (Média Longa)
Figure.add_trace(
    go.Scatter(
        x=Base_dados.index,
        y=Media_Tendencia,
        mode='lines',
        name='Média Tendência 30 dias',
        line=dict(color='#0bc83b', dash='dot'),
        opacity=0.7
    )
)

# Layout do gráfico
Figure.update_layout(
    title='Análise do Fechamento do Bitcoin com Médias Móveis',
    title_font_size=22,
    xaxis_title='Período Histórico',
    yaxis_title='Preço de Fechamento (USD)',
    template='plotly_dark',
    xaxis_title_font=dict(size=16),
    yaxis_title_font=dict(size=16),
    xaxis_tickfont=dict(size=12),
    yaxis_tickfont=dict(size=12)
)

# Exibindo o gráfico
Figure.show()
