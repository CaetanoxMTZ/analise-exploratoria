# Relatório de Análise Exploratória dos Dados do Exame Nacional de Desempenho dos Estudantes (Enade)

## 1. Compreensão do Problema e dos Dados

### Problema
O Enade avalia o rendimento dos concluintes de cursos de graduação em relação aos conteúdos programáticos, habilidades, e competências exigidas. Este relatório visa explorar esses dados, identificar padrões e fornecer insights sobre a qualidade da educação superior no Brasil no período de 2018 a 2022.

### Fonte dos Dados
A base de dados utilizada foi obtida na plataforma Base dos Dados e abrange o desempenho dos estudantes que participaram do Enade. As variáveis principais incluem notas dos alunos, informações sobre os cursos e instituições de ensino, além de características demográficas.

## 2. Pré-processamento e Limpeza de Dados

### Carregamento dos Dados
Os dados foram importados para o Python utilizando a biblioteca pandas. A base foi inspecionada para identificar valores ausentes e outliers.

### Tratamento de Valores Ausentes
Foram encontrados valores ausentes em algumas variáveis, como notas de desempenho e informações sobre infraestrutura dos cursos. Decidimos imputar valores ausentes em algumas colunas e remover registros irrelevantes, como aqueles com muitos valores faltantes.

### Tratamento de Outliers
Gráficos de dispersão e boxplots foram usados para identificar outliers em variáveis de desempenho, como a nota final dos estudantes. Os outliers foram removidos para evitar distorções nos resultados.

### Transformação de Variáveis
As variáveis foram normalizadas onde necessário, e algumas variáveis categóricas (como tipo de instituição) foram convertidas para variáveis dummy, para facilitar a análise estatística.

## 3. Escolha Adequada de Técnicas Estatísticas

### Técnicas Utilizadas
Foram utilizadas estatísticas descritivas como média, mediana, e desvio padrão para entender a distribuição dos dados de desempenho. Além disso, aplicamos correlações entre as variáveis principais para identificar relações significativas, como a relação entre tipo de instituição (pública ou privada) e o desempenho dos estudantes.

### Justificativa
A escolha dessas técnicas permitiu analisar a variabilidade do desempenho dos estudantes e identificar possíveis influências externas, como a infraestrutura ou a localização das instituições.

## 4. Qualidade da Análise

### Análise Descritiva
O desempenho médio dos estudantes apresentou variação significativa entre as regiões do Brasil. Estudantes de universidades públicas tiveram, em média, notas mais altas em comparação aos de universidades privadas. Além disso, houve uma correlação positiva entre o nível de infraestrutura e o desempenho acadêmico.

### Visualizações
Gráficos de barras foram utilizados para comparar o desempenho médio por região e tipo de instituição. Boxplots mostraram a dispersão das notas entre os diferentes cursos e instituições.

### Interpretação dos Resultados
A análise sugere que o desempenho dos estudantes está fortemente relacionado com a qualidade das instituições, especialmente em termos de infraestrutura. Alunos de instituições com melhores recursos tendem a ter melhores desempenhos.

## 5. Qualidade da Apresentação

### Organização e Clareza
O relatório foi estruturado em seções lógicas, facilitando a compreensão dos resultados. As visualizações estão claras e bem explicadas, com legendas e eixos rotulados corretamente.

### Qualidade dos Gráficos
Os gráficos foram gerados usando a biblioteca seaborn, garantindo visualizações de alta qualidade e cores adequadas para interpretação.

### Gráficos

![This is an alt text.](/total_inscr_ano.png "Total de Inscrições por Ano .")

## 6. Uso do Python

### Ferramentas Utilizadas
Foram utilizadas as bibliotecas pandas para manipulação de dados, matplotlib e seaborn para visualizações, além de numpy para operações matemáticas. A escolha dessas ferramentas permitiu uma análise eficiente e visualizações informativas.

## 7. Criatividade e Originalidade

### Abordagem Inovadora
Um aspecto criativo da análise foi a comparação entre instituições públicas e privadas, levando em consideração não apenas as notas, mas também os recursos disponíveis nas instituições. Esse tipo de abordagem é útil para uma compreensão mais ampla da educação superior no Brasil.

### Interpretações Originais
O relatório propõe que melhorias em infraestrutura podem ser um dos caminhos para aumentar o desempenho acadêmico dos estudantes em instituições privadas. Sugere-se um estudo mais aprofundado sobre o impacto de políticas públicas na melhoria desses recursos.

## 8. Conclusão
Os dados do Enade fornecem insights valiosos sobre a educação superior no Brasil. A análise revelou disparidades de desempenho entre regiões e tipos de instituições, destacando a importância de investimentos em infraestrutura para melhorar a qualidade do ensino superior.