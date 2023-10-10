import sqlite3
import csv
import io
from PIL import Image

# Nome do arquivo do banco de dados SQLite
nome_do_banco_de_dados = "dados_quotes.db"


# Função para ler o conteúdo de um arquivo CSV como uma lista de dicionários
def ler_csv(nome_arquivo):
    with open(nome_arquivo, mode="r", newline="") as arquivo_csv:
        reader = csv.DictReader(arquivo_csv)
        return [row for row in reader]


# Função para converter uma imagem em formato binário
def imagem_para_binario(nome_arquivo_imagem):
    with open(nome_arquivo_imagem, "rb") as arquivo_imagem:
        return arquivo_imagem.read()


# Estabeleça uma conexão com o banco de dados (ou crie um novo se não existir)
conexao = sqlite3.connect(nome_do_banco_de_dados)

# Crie um cursor para executar consultas SQL
cursor = conexao.cursor()

# Crie uma tabela QUOTE para armazenar os dados do CSV e a imagem binária
cursor.execute(
    """CREATE TABLE IF NOT EXISTS QUOTE (
                   id INTEGER PRIMARY KEY,
                   dados_csv BLOB,
                   imagem BLOB)"""
)

# Leia o conteúdo do arquivo CSV e converta para binário
dados_csv = ler_csv("dados.csv")
dados_csv_binario = io.StringIO()
csv_writer = csv.DictWriter(dados_csv_binario, fieldnames=dados_csv[0].keys())
csv_writer.writeheader()
csv_writer.writerows(dados_csv)
dados_csv_binario = dados_csv_binario.getvalue().encode()

# Converta a imagem para binário
imagem_binario = imagem_para_binario("imagem.jpg")

# Insira os dados na tabela QUOTE
cursor.execute(
    "INSERT INTO QUOTE (dados_csv, imagem) VALUES (?, ?)",
    (dados_csv_binario, imagem_binario),
)

# Execute uma consulta SQL para recuperar os dados
cursor.execute("SELECT * FROM QUOTE")
quote = cursor.fetchone()

# Recupere os dados do CSV e converta de volta para uma lista de dicionários
dados_csv_recuperados = csv.DictReader(io.StringIO(quote[1].decode()))
dados_csv_recuperados = [row for row in dados_csv_recuperados]

# Recupere a imagem e salve-a em um arquivo
imagem_recuperada = Image.open(io.BytesIO(quote[2]))
imagem_recuperada.save("imagem_recuperada.jpg")

# Salve as alterações no banco de dados e feche a conexão
conexao.commit()
conexao.close()
