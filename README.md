# Web Scraper e Analisador de Notícias por Tema (G1)

Este projeto coleta manchetes de diferentes seções do portal **G1** (como Economia, Política, Mundo, Tecnologia e Esportes), organiza as notícias por tema, analisa as palavras mais frequentes e exibe os resultados em gráficos.

O objetivo é demonstrar habilidades em **Web Scraping**, **Análise de Dados** e **Visualização**, utilizando ferramentas amplamente usadas em Data Science com Python.

---

## Funcionalidades

- Coleta automática de manchetes do G1 e GE (Esportes)
- Separação das notícias por tema (Economia, Política, Mundo, Tecnologia, Esportes)
- Contagem das palavras mais frequentes em cada tema
- Geração de gráficos de barras com as palavras mais usadas por categoria
- Salvamento dos dados em CSV (em `data/raw` e `data/processed`)
- Código modular, dividido em etapas claras de scraping, análise e visualização

---

## Tecnologias Utilizadas

- **Python 3.11+**
- **requests** → realiza as requisições HTTP
- **beautifulsoup4** → faz o parsing e extração de dados do HTML
- **pandas** → organiza e manipula os dados coletados
- **matplotlib** → gera gráficos de barras para visualização dos resultados

---

## Estrutura do Projeto

```bash
web-scraper-analyzer/
│
├── data/
│   ├── raw/                   # Dados brutos coletados do G1
│   │   └── g1_news_by_section.csv
│   └── processed/             # Dados analisados e tratados
│       └── frequency_by_theme.csv
│
├── src/
│   ├── scraper.py             # Faz o scraping por tema
│   ├── analyzer.py            # Analisa as palavras por tema
│   └── visualizer.py          # Gera gráficos com os resultados
│
├── requirements.txt           # Dependências do projeto
└── README.md                  # Documentação do projeto
```

---

## 🚀 Como Executar

Clone o repositório e instale as dependências:

```bash
git clone https://github.com/seuusuario/web-scraper-analyzer.git
pip install -r requirements.txt
```

### Coletar as notícias

O script abaixo faz scraping das seções de Economia, Política, Mundo, Tecnologia e Esportes do G1 e salva os dados em CSV.

```bash
python src/scraper.py
```

> O arquivo gerado será salvo em: data/raw/g1_news_by_section.csv

---

### Analisar as palavras mais frequentes

O script abaixo lê o CSV de notícias e calcula as palavras mais comuns em cada tema.

```bash
python src/analyzer.py
```

> O resultado é salvo em: data/processed/frequency_by_theme.csv

---

### Visualizar os resultados

O script abaixo cria um gráfico de barras para cada tema, mostrando as 10 palavras mais frequentes.

```bash
python src/visualizer.py
```

> Cada gráfico será exibido automaticamente com o Matplotlib.

---

## Exemplo de Resultado

Cada gráfico mostra as **10 palavras mais frequentes** em manchetes de um determinado tema.  
Por exemplo, para Economia:

```
Palavras mais frequentes em Economia:
- inflação
- dólar
- preço
- mercado
- governo
...
```

E um gráfico de barras é gerado como este:

```
---------------------------------------
|     Palavras mais frequentes        |
|          em Economia                |
---------------------------------------
```

---

## Arquivos Gerados

| Tipo              | Caminho                                 | Descrição                                                  |
| ----------------- | --------------------------------------- | ---------------------------------------------------------- |
| Dados brutos      | `data/raw/g1_news_by_section.csv`       | Contém todas as notícias coletadas com título, link e tema |
| Dados processados | `data/processed/frequency_by_theme.csv` | Contém as palavras mais frequentes por tema                |
| Visualização      | (gerado dinamicamente)                  | Gráficos de barras para cada tema                          |

---

## Exemplo de Dados

### `data/raw/g1_news_by_section.csv`

| tema       | titulo                          | link                     |
| ---------- | ------------------------------- | ------------------------ |
| economia   | Inflação desacelera em setembro | https://g1.globo.com/... |
| esportes   | Flamengo vence e avança na Copa | https://ge.globo.com/... |
| tecnologia | Apple lança novo iPhone         | https://g1.globo.com/... |

### `data/processed/frequency_by_theme.csv`

| tema       | palavra  | frequencia |
| ---------- | -------- | ---------- |
| economia   | inflação | 12         |
| economia   | mercado  | 9          |
| tecnologia | apple    | 15         |
| esportes   | flamengo | 8          |

---

## Ideias Futuras

- Agendar a coleta de notícias diariamente (com cron ou Task Scheduler)
- Gerar nuvem de palavras com a biblioteca `wordcloud`
- Criar um painel interativo com `plotly` ou `dash`
- Adicionar análise de sentimento com `textblob` ou `nltk`
- Exportar resultados em JSON ou Excel
- Criar um relatório HTML automatizado

---

## Boas Práticas Aplicadas

- Código organizado em **módulos independentes** (`scraper`, `analyzer`, `visualizer`)
- **Tratamento de exceções** para evitar falhas em requisições HTTP
- **Pausa automática (`sleep`)** entre requisições para respeitar o servidor
- **Documentação clara** com comentários e separação de responsabilidades
- **Uso de DataFrames** para limpeza e manipulação de dados

---

## Autor

Desenvolvido por **Yuri amaral santos**  
E-mail: yuri.a.santos12@gmail.com
Portfolio: https://yuri-amaral-santos-portfolio.vercel.app

---
