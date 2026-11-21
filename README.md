# Práticas de Ciência de Dados — atributos e pipeline

Atividades do período 2026/2 com a base Tips: criação de atributos, preparação de dados e aplicação de uma receita de pré-processamento em dados novos.

## Arquivos

- `01_criacao_de_atributos.ipynb`: atividades e análises de criação de atributos, com saídas executadas.
- `02_pipeline_pre_processamento.ipynb`: limpeza, atributos, codificação, alinhamento de colunas e padronização aprendida no histórico.
- `app.py`: exemplo de painel apresentado na prática de pipeline.
- `app_completo.py`: painel com os indicadores e o gráfico solicitados.
- `pipeline.py`: funções de preparação extraídas do notebook.
- `historico_pronto.csv` e `semana_pronta.csv`: resultados do pipeline.
- `resultados/atributos_tips.csv`: base enriquecida da primeira prática.
- `dados/tips.csv`: cópia local da base original para reprodução.

## Executar

Em Python 3.12, crie e ative um ambiente virtual e instale as dependências:

```sh
python -m pip install -r requirements.txt
jupyter notebook
```

Abra e execute os notebooks a partir desta pasta. As saídas já estão incluídas. Para abrir o painel:

```sh
python -m streamlit run app_completo.py
```

Selecione **Usar a semana de exemplo** ou envie um CSV com as sete colunas originais da base Tips, na mesma ordem: `total_bill,tip,sex,smoker,day,time,size`. Os valores monetários da base são tratados como dólares. Não há conversão para reais.

## Decisões e resultados

Na primeira prática, a remoção de uma duplicata deixa 243 registros. A criação dos atributos permite comparar o valor por pessoa e a gorjeta proporcional à conta. As conclusões são descritivas: diferenças entre grupos não demonstram causalidade.

Na segunda prática, a separação ocorre antes da preparação: os primeiros 200 registros formam o histórico e os 44 seguintes formam a semana. A limpeza é feita separadamente, conforme a atividade. Há uma duplicata entre os dois períodos da base original, por isso a soma dessas partições permanece em 244, enquanto a remoção global da primeira prática deixa 243.

A média e o desvio-padrão amostral usados para padronização são calculados somente no histórico. A semana reaproveita esses parâmetros e o esquema de colunas do histórico, evitando aprender a transformação com os dados novos. As duas saídas têm 15 colunas e nenhum valor ausente.

O painel usa a média do percentual de gorjeta por mesa e a média do gasto por pessoa. Não confunde a média das razões com a razão dos totais. Na semana de exemplo, os indicadores exibem **15,2%** e **US$ 7,75**. A sinalização acima de dois desvios é um critério exploratório, não uma prova de erro nos dados.

## Verificação

Os dois notebooks foram executados integralmente: 30 células de código, sem exceções e sem respostas em branco. O painel foi conferido com `streamlit.testing.v1.AppTest`, incluindo a seleção da semana de exemplo, os dois indicadores, o gráfico e as duas tabelas.

## Fonte

Base pública [Tips, no repositório seaborn-data](https://github.com/mwaskom/seaborn-data/blob/master/tips.csv), utilizada pelos notebooks da disciplina. SHA-256 da cópia local: `e54cc4d2ce1bff65d32ca60b3e4b802e06bde1d7e7caf6f796f6bf7370e863b0`.
