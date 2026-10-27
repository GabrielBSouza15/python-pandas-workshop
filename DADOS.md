# Bases sintéticas de ensino

Todos os registros foram criados para esta edição. Não são anonimizações de bases reais, não foram amostrados das bases do Drive e não descrevem pessoas ou organizações reais. Valores monetários representam unidades fictícias e não podem ser interpretados como salários ou resultados profissionais.

| Arquivo | Linhas | Colunas e finalidade |
|---|---:|---|
| vendas.csv | 6 | id_venda, data_venda, nome_produto, quantidade, valor_unitario, valor_total; leitura/exportação CSV e Excel |
| player_stats.csv | 4 | name, team, age, played, goals; preservar zeros legítimos e reconhecer idade ausente |
| player_salaries.csv | 8 | Player, Nation, Position, Team, Age, Annual; uma linha integral repetida e ausências para comparar critérios de limpeza |
| dados_funcionarios.csv | 7 | ID, Nome, Departamento, Idade, Salario, Anos_Experiencia; uma linha integral repetida e campos ausentes para agrupamento e gráficos |

CSV em UTF-8, separado por vírgulas, com ponto decimal. Campo vazio significa valor desconhecido. Os períodos são referências didáticas fixas; não indicam quando o minicurso aconteceu.

Os notebooks geram esses dados dentro de `minicurso_pandas_dados/`. Os resultados são gravados em `minicurso_pandas_saidas/`, incluindo exportações de treino e o gráfico do gabarito. Ambas as pastas estão no `.gitignore`.

O fato de esta base usar algumas repetições integrais intencionais não autoriza remover registros repetidos de qualquer base real. A escolha depende da identificação dos registros e da regra de negócio.
