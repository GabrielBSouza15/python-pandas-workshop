# Minicurso de Python e pandas

Material do minicurso organizado e ministrado por **Gabriel Bitencourt de Souza** na Semana Acadêmica de Engenharia de Produção da UFV. Gabriel liderou o planejamento e a elaboração do material com a equipe e realizou a apresentação principal. Na atividade, as 20 vagas foram preenchidas e a avaliação informada pelos participantes foi de 4,7/5.

O material reúne exemplos executáveis, três exercícios e um gabarito comentado para prática no Google Colab ou Jupyter. **Todas as bases são sintéticas.** Atletas, clubes, pessoas, salários e vendas são fictícios.

## Começar

- [Abrir o minicurso no Google Colab](https://colab.research.google.com/github/GabrielBSouza15/python-pandas-workshop/blob/main/WorkshopPandas.ipynb)
- [Ler o notebook no GitHub](WorkshopPandas.ipynb)
- [Abrir o gabarito no Google Colab](https://colab.research.google.com/github/GabrielBSouza15/python-pandas-workshop/blob/main/WorkshopPandas_gabarito.ipynb)
- [Consultar o dicionário das bases](DADOS.md)

No Colab, conecte-se ao ambiente Python e execute as células em ordem. O notebook prepara seus próprios dados sintéticos: **não é necessário montar o Drive, fornecer credenciais ou enviar arquivos pessoais**. As pastas `minicurso_pandas_dados/` e `minicurso_pandas_saidas/` são usadas e recriadas para os exemplos; não coloque arquivos pessoais nelas.

Pré-requisitos: variáveis, listas, dicionários e comparações básicas em Python.

## Conteúdo

1. Series, DataFrames, rótulos e posições.
2. Leitura e exportação de CSV e Excel.
3. Seleção, filtros booleanos, ordenação e índices.
4. Ausências, repetições e conversão de datas.
5. `groupby`, agregação, `count` versus `size` e tabelas dinâmicas.
6. Gráficos com pandas e Matplotlib.
7. Três exercícios integradores com soluções e verificações de resultados.

O minicurso é introdutório. O conteúdo aborda decisões de análise: zero não equivale a dado ausente, preencher salário com zero pode distorcer resultados, e eliminar todas as linhas incompletas pode introduzir viés.

![Exemplo do gabarito com dados sintéticos: médias conhecidas, quantidade de pessoas e distribuição de idades](exemplo_agrupamento.png)

## Executar localmente

Com Python 3.10 ou superior, preferencialmente em ambiente virtual:

```bash
python -m pip install -r requirements.txt
python -m jupyterlab
```

Abra um dos notebooks e execute desde a primeira célula. Os CSVs da raiz permitem examinar os exemplos sem executar código; os notebooks geram cópias equivalentes nas pastas de demonstração. O XLSX de treino é criado durante a preparação usando somente o CSV sintético.

## Validação

Consulte [VALIDACAO.md](VALIDACAO.md) para o ambiente e os testes executados.

As referências técnicas estão nos notebooks. A organização do material de apoio e do gabarito contou com apoio do OpenAI Codex. Gabriel liderou a preparação do minicurso com a equipe e realizou a apresentação principal.

[Gabriel Bitencourt de Souza no LinkedIn](https://www.linkedin.com/in/gabrielbitencourtdesouza/)


## Verificação automática

O workflow executa os dois notebooks em kernels e pastas temporárias independentes, incluindo as verificações do gabarito. Os notebooks publicados continuam sem saídas de execução; nenhum dado pessoal é necessário. A execução ocorre em alterações de `main`, pull requests e acionamentos manuais. Consulte o resultado em [GitHub Actions](https://github.com/GabrielBSouza15/python-pandas-workshop/actions/workflows/testes.yml).

## Licença

[MIT](LICENSE), para o conteúdo publicado neste repositório.
