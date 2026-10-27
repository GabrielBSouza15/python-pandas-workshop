# Validação do minicurso

26/10/2026.

- Python 3.12.14, pandas 3.0.1 e Matplotlib 3.11.2.
- Os dois notebooks têm 79 células, sendo 19 de código cada.
- Todas as células de código executadas em ordem em uma sessão IPython local independente para cada notebook, sem erros.
- Gabarito com 30 verificações de resultados (`assert` e comparações de DataFrames): contagem de linhas, preservação de zeros, ausências, filtros, ordenação, índices, médias, agregações e exportações CSV/Excel lidas de volta.
- Sintaxe de todos os blocos Python em Markdown conferida separadamente.
- Formato dos notebooks validado com nbformat.
- Gráfico do exercício de agrupamento gerado e inspecionado visualmente.
- Notebooks públicos sem saídas de execução, credenciais, URLs privadas ou metadados de contas pessoais. As pastas de execução ficam fora do repositório.

O caminho de execução validado foi local. Não foi feita uma execução automatizada dentro de uma sessão remota do Google Colab. A abertura dos links do Colab é uma conferência separada da execução. O intervalo de dependências em requirements.txt não implica teste de todas as versões permitidas; o ambiente acima é o que foi efetivamente usado.

## Resultados de referência do gabarito

- Média dos gols sintéticos: **1,75**, preservando zeros.
- Idade ausente no exemplo inicial: **1** ocorrência.
- Após a remoção da repetição integral, comparação de salários conhecidos e idade válida: **Atleta fictício C** aparece em primeiro. A remoção global de linhas incompletas exclui esse registro por posição ausente e mudaria o primeiro para **Atleta fictício B**.
- RH tem **2** pessoas fictícias e **1** salário conhecido: `size` e `count` representam perguntas diferentes.
- TI tem média salarial conhecida de **5.500** e soma conhecida de **11.000**, em unidades fictícias.

Esses resultados são exemplos de ensino, sem relação com pessoas, organizações ou resultados profissionais reais.
