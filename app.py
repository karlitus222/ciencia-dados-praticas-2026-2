from pathlib import Path
import pandas as pd
import streamlit as st

URL = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"


def limpar(df):
    df = df.copy()
    df.columns = ["conta", "gorjeta", "sexo", "fumante", "dia", "turno", "pessoas"]
    return df.drop_duplicates()


def criar_atributos(df):
    df = df.copy()
    df["percentual_gorjeta"] = df["gorjeta"] / df["conta"] * 100
    df["conta_por_pessoa"] = df["conta"] / df["pessoas"]
    return df


historico = criar_atributos(limpar(pd.read_csv(Path(__file__).parent / 'dados' / 'tips.csv').iloc[:200]))
receita = {"media": historico["percentual_gorjeta"].mean(), "desvio": historico["percentual_gorjeta"].std()}

st.title("Gorjetas da semana")
arquivo = st.file_uploader("Envie o CSV da semana", type="csv")
usar_exemplo = st.checkbox("Usar a semana de exemplo")

if arquivo is not None or usar_exemplo:
    dados = pd.read_csv(arquivo) if arquivo is not None else pd.read_csv(Path(__file__).parent / 'dados' / 'tips.csv').iloc[200:]
    semana = criar_atributos(limpar(dados))
    semana["percentual_z"] = (semana["percentual_gorjeta"] - receita["media"]) / receita["desvio"]
    st.metric("Percentual médio da semana", f"{semana['percentual_gorjeta'].mean():.1f}%",
              f"{semana['percentual_gorjeta'].mean() - receita['media']:.1f} p.p. em relação ao histórico")
    st.subheader("Mesas fora do padrão (mais de 2 desvios)")
    st.dataframe(semana[semana["percentual_z"].abs() > 2])
    st.subheader("Base da semana preparada")
    st.dataframe(semana)
