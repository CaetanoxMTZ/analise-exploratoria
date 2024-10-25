import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
from google.oauth2 import service_account
from pandas_gbq import read_gbq
from dotenv import load_dotenv
import os


load_dotenv()

def carregar_dados(query, project_id, credentials_file, location='US'):
    try:
        credentials = service_account.Credentials.from_service_account_file(credentials_file)

        dados = read_gbq(query, project_id=project_id, credentials=credentials, location=location)
        print(f"Dados carregados com sucesso: {len(dados)} linhas e {len(dados.columns)} colunas.")
        return dados
    except Exception as e:
        print(f"Erro ao carregar os dados: {e}")
        return None

def explorar_dados(dados):
    print("\nResumo dos Dados:")
    print(dados.describe())
    print("\nTipos de Dados:")
    print(dados.dtypes)
    print("\nValores Ausentes:")
    print(dados.isnull().sum())

    fig = px.box(dados.select_dtypes(include=[np.number]), title='Visualização de Outliers', points='all')
    fig.show()

def tratar_valores_ausentes(dados):
    for coluna in dados.columns:
        if dados[coluna].isnull().sum() > 0:
            if np.issubdtype(dados[coluna].dtype, np.number):
                dados[coluna].fillna(dados[coluna].mean(), inplace=True)
            else:
                if not dados[coluna].mode().empty:
                    dados[coluna].fillna(dados[coluna].mode()[0], inplace=True)
    return dados

def tratar_outliers(dados):
    for coluna in dados.select_dtypes(include=[np.number]).columns:
        Q1 = dados[coluna].quantile(0.25)
        Q3 = dados[coluna].quantile(0.75)
        IQR = Q3 - Q1
        limite_inferior = Q1 - 1.5 * IQR
        limite_superior = Q3 + 1.5 * IQR
        dados = dados[(dados[coluna] >= limite_inferior) & (dados[coluna] <= limite_superior)]
    return dados

def calcular_estatisticas_descritivas(dados):
    estatisticas = dados.describe()
    print(estatisticas)

def visualizar_dados(dados):
    # Converter ano para numérico, se necessário
    dados['ano'] = pd.to_numeric(dados['ano'], errors='coerce')

    # Criar uma métrica agregada por ano para evitar uma linha reta
    dados_agrupados = dados.groupby('ano').size().reset_index(name='total_inscricoes')


    if len(dados_agrupados['total_inscricoes'].unique()) == 1:
        print("Aviso: Todos os anos têm o mesmo número de inscrições. O gráfico pode aparecer como uma linha reta.")


    fig = px.line(dados_agrupados, x='ano', y='total_inscricoes', title='Total de Inscrições por Ano', markers=True)
    fig.update_layout(xaxis_title='Ano', yaxis_title='Total de Inscrições')
    fig.show()


    if dados.select_dtypes(include=[np.number]).shape[1] > 1:
        fig = px.imshow(dados.corr(), text_auto=True, title='Mapa de Correlação', color_continuous_scale='coolwarm')
        fig.show()
    else:
        print("Aviso: Não há variáveis numéricas suficientes para calcular a correlação.")


    if not dados.empty:
        fig = px.histogram(dados.melt(), x='value', facet_col='variable', title='Distribuição das Variáveis', nbins=20)
        fig.show()
    else:
        print("Aviso: Dados insuficientes para gerar histogramas.")

def apresentar_resultados():
    print("Análise concluída. Consulte os gráficos e estatísticas descritivas apresentadas.")

def main():

    QUERY = """
    SELECT ano, id_inscricao, faixa_etaria, sexo, id_municipio_residencia, sigla_uf_residencia
    FROM `basedosdados.br_inep_enem.microdados`
    WHERE ano BETWEEN 2018 AND 2022

    """


    PROJECT_ID = os.getenv('id_projeto_cloud_console')
    CREDENTIALS_FILE = os.getenv('arquivo_credenciais_cloud_console')
    LOCATION =  os.getenv('localidade_cloud_console')

    dados = carregar_dados(QUERY, PROJECT_ID, CREDENTIALS_FILE, location=LOCATION)
    if dados is not None:
        explorar_dados(dados)

        dados = tratar_valores_ausentes(dados)
        dados = tratar_outliers(dados)

        calcular_estatisticas_descritivas(dados)

        visualizar_dados(dados)

        apresentar_resultados()

if __name__ == "__main__":
    main()