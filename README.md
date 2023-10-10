# Documentação do Projeto - Desafio Crawler

## Introdução

Este projeto foi desenvolvido como parte de um desafio de web scraping para extrair dados de um site e disponibilizá-los em formatos estruturados (CSV). O objetivo principal é automatizar o processo de coleta de citações de um site específico e permitir que o usuário escolha como gostaria de receber essas citações.

## Funcionalidades

O projeto consiste em três partes principais:

- **quote.py**: Esta é a biblioteca que contém as funcionalidades para realizar o web scraping do site "quotes.toscrape" e extrair as informações desejadas. Ela também inclui a geração de screenshots.

- **main.py**: Este é o programa principal que permite ao usuário interagir com a biblioteca `quote.py` através de uma interface de linha de comando. O usuário pode escolher entre ver citações por autor, ver citações por tag ou sair do programa.

- **selenium.py**: Este módulo usa o Selenium para tirar screenshots em tela cheia do site "quotes.toscrape".

## Como Executar com Docker

Você pode executar este projeto dentro de um contêiner Docker sem a necessidade de instalar dependências no ambiente local. Siga estas etapas:

### Build do Contêiner

Certifique-se de ter o Docker instalado em seu sistema.

1. Clone este repositório em seu computador:



3. Execute o comando de build do Docker para criar a imagem do contêiner:

```bash
docker build -t nome-da-imagem .7
```

### Execução do Contêiner

4. Agora, você pode executar o contêiner Docker criado com o seguinte comando:

```bash
docker run -it nome-da-imagem
```



Isso iniciará o programa principal dentro do contêiner Docker, onde você pode interagir com o web scraping.

5. Siga as instruções exibidas no terminal para selecionar a opção desejada (ver citações por autor, ver citações por tag ou sair).

## Resultado

As citações serão salvas em arquivos CSV, e screenshots também serão capturadas e salvas dentro do contêiner Docker.

## Exemplo de Uso

Aqui está um exemplo de como usar o programa:

1. Ao executar o contêiner Docker, você pode escolher a opção "Ver citações por autor".

2. O programa exibirá uma lista de autores disponíveis. Digite o nome de um autor.

3. O programa extrairá e salvará as citações desse autor em um arquivo CSV e também criará uma screenshot da página.

4. Você pode repetir o processo para ver citações por tag ou sair do programa.

## Considerações Finais

Este é um projeto básico de web scraping que demonstra como extrair informações de um site e oferece alguma flexibilidade ao usuário para escolher as consultas desejadas. Lembre-se de ajustar o código e a documentação de acordo com suas necessidades específicas.

**Nota:** Certifique-se de respeitar os termos de uso do site que você está raspando e considere a ética e a legalidade ao usar essas técnicas.


