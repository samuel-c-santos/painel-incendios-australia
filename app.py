import pandas as pd
import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Carregar os dados
df = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Historical_Wildfires.csv')
df['Mês'] = pd.to_datetime(df['Date']).dt.month_name(locale='pt_BR')  # Converter datas para nomes de meses em português
df['Ano'] = pd.to_datetime(df['Date']).dt.year  # Extrair o ano

# Criar a aplicação Dash
app = dash.Dash(__name__)

# Layout da aplicação
app.layout = html.Div([
    html.H1(
        'PAINEL DE INCÊNDIOS FLORESTAIS NA AUSTRÁLIA', 
        style={
            'textAlign': 'center', 
            'color': '#2C3E50', 
            'font-size': 28, 
            'font-family': 'Helvetica Bold',
            'text-transform': 'uppercase'
        }
    ),
    
    html.Div([
        html.Div([
            html.H3(
                'Selecione a Região:', 
                style={
                    'margin-right': '1em', 
                    'font-family': 'Helvetica'
                }
            ),
            dcc.RadioItems(
                options=[
                    {'label': 'Nova Gales do Sul', 'value': 'NSW'},
                    {'label': 'Território do Norte', 'value': 'NT'},
                    {'label': 'Queensland', 'value': 'QL'},
                    {'label': 'Austrália do Sul', 'value': 'SA'},
                    {'label': 'Tasmânia', 'value': 'TA'},
                    {'label': 'Vitória', 'value': 'VI'},
                    {'label': 'Austrália Ocidental', 'value': 'WA'}
                ],
                value='NSW',
                id='regiao',
                inline=True,
                style={
                    'font-family': 'Helvetica'
                }
            ),
        ], style={'flex': 1}),
        html.Div([
            html.H3(
                'Selecione o Ano:', 
                style={
                    'margin-right': '1em', 
                    'font-family': 'Helvetica'
                }
            ),
            dcc.Dropdown(
                df['Ano'].unique(), 
                value=2005, 
                id='ano', 
                placeholder='Selecione um ano',
                style={
                    'width': '100%', 
                    'font-family': 'Helvetica'
                }
            )
        ], style={'flex': 1})
    ], style={
        'display': 'flex', 
        'align-items': 'center', 
        'justify-content': 'space-between', 
        'margin-bottom': '2em'
    }),

    html.Div([
        html.Div([], id='grafico1', style={'flex': 1, 'padding': '1em'}),
        html.Div([], id='grafico2', style={'flex': 1, 'padding': '1em'})
    ], style={'display': 'flex', 'justify-content': 'center'})
])

# Callback para atualizar os gráficos
@app.callback(
    [Output('grafico1', 'children'), Output('grafico2', 'children')],
    [Input('regiao', 'value'), Input('ano', 'value')]
)
def atualizar_graficos(regiao_selecionada, ano_selecionado):
    dados_filtrados = df[(df['Region'] == regiao_selecionada) & (df['Ano'] == ano_selecionado)]
    
    # Gráfico de rosca
    dados_rosca = dados_filtrados.groupby('Mês')['Estimated_fire_area'].mean().reset_index()
    fig1 = px.pie(
        dados_rosca, 
        values='Estimated_fire_area', 
        names='Mês', 
        title=f'{regiao_selecionada}: Média Mensal da Área Estimada de Incêndios em {ano_selecionado}',
        hole=0.4,  # Configurar o gráfico como rosca
        color_discrete_sequence=px.colors.sequential.YlOrRd
    )
    fig1.update_layout(
        font_family='Helvetica',
        title_font_family='Helvetica Bold'
    )
    
    # Gráfico de barras
    dados_barras = dados_filtrados.groupby('Mês')['Count'].mean().reset_index()
    fig2 = px.bar(
        dados_barras, 
        x='Mês', 
        y='Count', 
        title=f'{regiao_selecionada}: Média de Ocorrências de Incêndios Vegetativos em {ano_selecionado}',
        color='Count',
        color_continuous_scale=px.colors.sequential.YlOrRd
    )
    fig2.update_layout(
        font_family='Helvetica',
        title_font_family='Helvetica Bold'
    )
    
    return dcc.Graph(figure=fig1), dcc.Graph(figure=fig2)

# Executar a aplicação
if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 8050))
    app.run_server(debug=False, host='0.0.0.0', port=port)
