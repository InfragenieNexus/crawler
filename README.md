# Documentação do Projeto - Desafio Crawler

O projeto Desafio Crawler foi desenvolvido com o objetivo de extrair dados de um site específico por meio de web scraping e disponibilizá-los em formatos estruturados (CSV). O principal propósito é automatizar a coleta de citações de um site e permitir que o usuário escolha como deseja receber essas citações.

## Funcionalidades


- [x]  Realizar a busca por dados de forma automatizada (por meio de um script de linha de comando ou interface clicável)
- [x]  Padronizar os retornos estruturados (json/csv)
- [x]  Implementar um sistema de registro para acompanhar a execução
- [x]  Fornecer prova da consulta (captura de tela)
- Extras:
    - [x]  Armazenar os resultados em um banco de dados relacional ou não-relacional
    - [x]  Criar um dataframe para visualizar os resultados usando o pandas
    - [x]  Capturar resultados dinamicamente sem fixar os caminhos xpath
    - [x]  Dockerizar a aplicação
    - [x]  Agendar a execução para uma data e horário específicos.



## Como Executar com Docker

Você pode executar este projeto dentro de um contêiner Docker, eliminando a necessidade de instalar dependências no ambiente local. Siga as etapas abaixo:

### Construção do Contêiner

Certifique-se de ter o Docker instalado em seu sistema.

1. Clone este repositório em seu computador.
2. Execute o comando de build do Docker para criar a imagem do contêiner:

```bash
docker build -t nome-da-imagem .
```
### Execução do Contêiner

1. Agora, você pode executar o contêiner Docker criado com o seguinte comando:

```bash
docker-compose up -d

```
2. Para acessar o terminal do contêiner:

```bash
docker run -it desafio_crawler /bin/bash

```
## Usando Make

Este projeto utiliza um Makefile para simplificar tarefas comuns de desenvolvimento, como formatação e verificação de código. A seguir, estão os comandos disponíveis no Makefile:

Para executar os comandos, abra um terminal no diretório raiz do projeto e execute o seguinte comando:

```bash
make format

```

Esse comando aplicará a formatação ao código Python no diretório atual e em subdiretórios, seguindo as convenções de estilo do black. É uma boa prática executar este comando antes de enviar seu código para revisão ou quando desejar manter uma formatação consistente.

```bash
make play-crawler

```

Esse comando iniciará a execução do projeto, que deve estar configurado no arquivo **main**.py.


## Resultados

As citações serão salvas em arquivos CSV, screenshots em formato PNG serão capturadas e salvas na pasta "output". Além disso, os dataframes pandas serão salvos no banco de dados e os screenshots também serão salvos no banco, ambos em formato binário, para facilitar consultas futuras.


## Janela de Interação

A janela de interação do Desafio Crawler permite ao usuário escolher como deseja receber as citações. As opções disponíveis são:

1. **Ver citações por autor**: O usuário pode buscar citações específicas de um autor selecionado.
2. **Ver citações por tag**: O usuário pode buscar citações relacionadas a uma tag específica.
3. **Ver todas as citações**: O usuário pode visualizar todas as citações disponíveis.
4. **Ver logs**: O usuário pode acessar e analisar os registros do processo de execução, caso ocorra uma falha ou para fins de análise.
5. **Sair**: O usuário pode sair do Desafio Crawler.

Essas interações permitem ao usuário personalizar a forma como ele recebe as citações e explorar diferentes aspectos do conteúdo disponível.


## Arquitetura do projeto 
```
|-- desafio_crawler
|   |-- logger
|   |   |-- log_script.py
|   |   |-- log_file.txt
|   |-- output
|   |   |-- csv_files
|   |   |   |-- search_results.csv
|   |   |-- screenshot
|   |   |   |-- screenshot.png
|   |-- chromedriver
|   |-- utils
|   |   |-- job.py
|   |   |-- scheduler.py
|   |   |-- name_generator.py
|   |   |-- logger.py
|   |   |-- requirements.txt
|   |   |-- start.sh
|   |-- main.py
|   |-- quote.py
|   |-- core_db.py
|   |-- makefile
|-- Dockerfile
|-- .env_sample
|-- .gitignore
|-- docker-compose.yml
|-- readme.md
```

A pasta "logger" contém um arquivo de script chamado `script.py` para exibir os logs do projeto, assim como um arquivo que pode ser lido para hospedar esses logs.

A pasta "output" armazena os arquivos CSV das buscas e o arquivo de captura de tela (screenshot).

O arquivo `chromedriver` é utilizado para abrir o Google.

Na pasta "utils", encontramos os seguintes arquivos:

- `job.py` que será utilizado para executar o cronjob futuramente.
- `scheduler.py` que é um script de interação onde o usuário pode escrever quando deseja agendar o cronjob.
- `name_generator.py` para criar nomes para o screenshot e os arquivos CSV das consultas.
- `logger.py` que carrega todos os scripts necessários para a biblioteca de log criar logs.

Na raiz da pasta "desafio_crawler", encontramos:

- `main.py` que é o script responsável por iniciar a interação com o usuário.
- `quote.py` onde está a classe responsável pelo web scraping.
- `core_db.py` que cuida da criação do banco de dados com SQLite e a inserção dos dados nele.



## Melhorias

A seguir, são apresentadas as melhorias sugeridas para o projeto Desafio Crawler, que serão documentadas formalmente:

1. Conclusão do cronjob.
2. Aperfeiçoamento do código para reduzir a dependência excessiva de xpath.
3. Aprimoramento da arquitetura do projeto.
4. Aumento do desempenho, considerando a utilização de paralelismo, threads e limitando-as.
5. Armazenamento de imagens e arquivos em um bucket da AWS.
6. Criação de testes, tanto de ponta a ponta quanto unitários.
7. Melhoria do Dockerfile, utilizando uma imagem mais oficial.
8. Adicionar uma biblioteca de tracing para acompanhar todo o processo e armazená-lo no banco de dados.

Essas melhorias contribuirão para aprimorar a funcionalidade, a eficiência e a confiabilidade do projeto Desafio Crawler.
