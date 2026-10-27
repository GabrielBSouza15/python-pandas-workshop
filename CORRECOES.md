# Correções e decisões da edição pública

Revisão do notebook apresentado em Colab. Referências oficiais consultadas em 26/10/2026.

| Ponto do material original | Correção |
|---|---|
| Célula incompleta com `impor` e leitura de arquivo de apartamentos que não está na pasta | Substituída por exportação CSV executável usando a base de vendas sintética |
| `line_terminator` na tabela de `to_csv` | Corrigido para `lineterminator` |
| `date_format` e `mode` atribuídos diretamente a `DataFrame.to_excel` | Movidos para o contexto de `pd.ExcelWriter`; incluída leitura de volta e exemplo de acréscimo de aba |
| Opção `strings_to_formulas` apresentada junto do openpyxl | Explicado que é específica do XlsxWriter; não passada ao openpyxl |
| `files.download` sem importação | Download tornou-se opcional; importação `from google.colab import files` explicitada e arquivos acessíveis pelo painel do Colab |
| `df['idade'].fillna(..., inplace=True)` | Substituído por atribuição explícita, compatível com Copy-on-Write |
| Todos os zeros da base esportiva tratados como ausência | Preservados gols e partidas iguais a zero; ausência explicitada somente onde o valor é desconhecido |
| Salário ausente preenchido com zero como orientação geral | Mantido como exemplo explicado de uma decisão que pode distorcer resultados; gabarito da análise preserva desconhecidos |
| Média da idade com uma linha repetida | Explicado que 27,25 inclui a repetição e que remover a repetição antes resulta em 28,0 |
| Remoção de todas as linhas incompletas antes do ranking | Comparada com `dropna(subset=...)` dos campos necessários; o exemplo mostra a mudança indevida do primeiro colocado |
| Duplicatas sugeridas a partir de nomes | Explicitado que nome igual não comprova repetição; remoção limitada às linhas integralmente repetidas de propósito |
| `count()` descrito como contagem de elementos sem ressalva | Diferenciado de `size()`: count exclui ausências na coluna, size conta linhas |
| Gráfico de linha para média por departamento | Substituído por barras, pois departamentos são categorias sem continuidade |
| Seção de datas sem conversão executável | Acrescentado `pd.to_datetime` com formato explícito e conferência das conversões para `NaT` |
| Relação entre loc e iloc pouco explícita nas fatias | Incluída a diferença entre inclusão do rótulo final em loc e exclusão da posição final em iloc |
| Texto de pivot com múltiplas agregações quando havia somente soma | Título corrigido para uma agregação e duas dimensões |
| Material dependente de upload manual de bases | Preparação sintética autocontida, sem Drive, tokens ou acesso a contas |

As estruturas, seleção, filtros, ordenação, limpeza, agrupamento, tabelas dinâmicas e visualização foram mantidos como temas. As alterações não significam que cada trecho original estava incorreto; várias esclarecem limites e tornam a prática reproduzível.

As bases recebidas de jogadores/salários, funcionários e vendas não traziam documentação suficiente de procedência e licença. A publicação utiliza novas bases sintéticas de pequeno porte, com os esquemas necessários aos exercícios. Não faz afirmações sobre remuneração ou desempenho de pessoas reais.

## Fontes oficiais

- [DataFrame.to_csv](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html)
- [DataFrame.to_excel](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_excel.html)
- [ExcelWriter](https://pandas.pydata.org/docs/reference/api/pandas.ExcelWriter.html)
- [Copy-on-Write](https://pandas.pydata.org/pandas-docs/version/3.0/user_guide/copy_on_write.html)
- [Tratamento de valores ausentes](https://pandas.pydata.org/docs/user_guide/missing_data.html)
- [Agrupamento e agregação](https://pandas.pydata.org/docs/user_guide/groupby.html)
- [Indexação e seleção](https://pandas.pydata.org/docs/user_guide/indexing.html)
