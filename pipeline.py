import pandas as pd
import numpy as np

def limpar(df):
    df = df.copy()
    df.columns = ["conta", "gorjeta", "sexo", "fumante", "dia", "turno", "pessoas"]
    return df.drop_duplicates()



def criar_atributos(df):
    df = df.copy()
    df['percentual_gorjeta'] = df['gorjeta'] / df['conta'] * 100
    df['conta_por_pessoa'] = df['conta'] / df['pessoas']
    df['fim_de_semana'] = df['dia'].isin(['Sat', 'Sun']).astype(int)
    df['grupo_grande'] = (df['pessoas'] >= 4).astype(int)
    df['faixa_conta'] = pd.cut(df['conta'], bins=[0, 15, 25, np.inf], labels=['baixa', 'média', 'alta'])
    return df

def codificar(df):
    df = df.copy()
    df['sexo'] = (df['sexo'] == 'Female').astype(int)
    df['fumante'] = (df['fumante'] == 'Yes').astype(int)
    df['faixa_conta'] = df['faixa_conta'].map({'baixa': 0, 'média': 1, 'alta': 2}).astype(int)
    df['turno'] = (df['turno'] == 'Dinner').astype(int)
    return pd.get_dummies(df, columns=['dia'], prefix='dia', dtype=int)
COLUNAS_PADRONIZAR = ["conta", "percentual_gorjeta", "conta_por_pessoa"]


def aprender_receita(historico):
    return {
        "colunas": list(historico.columns),
        "media": historico[COLUNAS_PADRONIZAR].mean(),
        "desvio": historico[COLUNAS_PADRONIZAR].std(),
    }


def aplicar_receita(df, receita):
    df = df.reindex(columns=receita["colunas"], fill_value=0).copy()
    df[COLUNAS_PADRONIZAR] = (df[COLUNAS_PADRONIZAR] - receita["media"]) / receita["desvio"]
    return df


def preparar(df_bruto, receita):
    df = limpar(df_bruto)
    df = criar_atributos(df)
    df = codificar(df)
    return aplicar_receita(df, receita)
